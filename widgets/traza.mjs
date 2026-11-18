// traza.mjs · Visualizador de trazas de AC Institut (anywidget para MyST / Jupyter Book 2)
// Muestra un programa ejecutándose paso a paso: línea ejecutada, casillas de la lista
// consultadas, variables, condiciones evaluadas, pantalla y tabla de traza.
// El modelo llega del cuerpo JSON de la directiva:  { "config": {...}, "traza": {...} }
// La traza la genera herramientas/trazar.py ejecutando el programa con sys.settrace.

// Los estilos van dentro del módulo (una <style> en el propio widget): así viajan con él
// y funcionan igual en el libro, en el blog o en cualquier página que cargue el módulo.
const ESTILOS = `
/* traza.css · estilos del visualizador (piel AC Institut, paleta vino) */
.tz{
  --acento:#7A1F36; --suave:#F6F0EE; --oscuro:#5A1628;
  --banda:#6B6B6B; --filete:#9A9A9A; --fila:#D4D4D4; --fondo:#F4F4F4; --sub:#333; --tinta:#111; --si:#2D5A48;
  --titulo:"Montserrat","Helvetica Neue",Arial,sans-serif; --texto:"Arimo","Liberation Sans",Arial,sans-serif; --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
  font:400 15px/1.55 var(--texto); color:var(--tinta); background:#fff;
  display:flex; flex-direction:column; gap:16px; padding:16px; border:1px solid var(--fila); border-radius:10px; margin:1.25rem 0;
}
.tz *{ box-sizing:border-box; }
.tz p{ margin:0; }
.tz-cab{ display:flex; justify-content:space-between; align-items:baseline; gap:10px; flex-wrap:wrap; }
.tz-tit{ font:700 18px/1.2 var(--titulo); }
.tz-etq{ font:600 10.5px/1 var(--titulo); letter-spacing:.1em; text-transform:uppercase; color:var(--acento); border:1.5px solid var(--acento); border-radius:6px; padding:5px 8px; }
.tz-idea{ border-left:4px solid var(--acento); padding:2px 0 2px 12px; color:var(--sub); }
.tz-escena{ display:grid; grid-template-columns:1fr 1fr; gap:16px; align-items:start; }
.tz-col{ display:flex; flex-direction:column; gap:12px; min-width:0; }
.tz-caja{ border:2px solid var(--tinta); background:#fff; }
.tz-barra{ background:var(--acento); color:#fff; padding:6px 12px; font:600 10.5px/1.2 var(--titulo); letter-spacing:.12em; text-transform:uppercase; display:flex; justify-content:space-between; gap:8px; }
.tz-barra.negro{ background:var(--tinta); }
.tz-micro{ font:600 10.5px/1.2 var(--titulo); letter-spacing:.12em; text-transform:uppercase; color:var(--banda); margin-bottom:6px !important; }
.tz-micro.acento{ color:var(--acento); margin:0 !important; }

pre.tz-codigo{ margin:0; font:400 14px/1.85 var(--mono); overflow-x:auto; background:var(--fondo); padding:6px 0; border:0; border-radius:0; }
.tz .ln{ display:flex; align-items:center; white-space:pre; padding-right:12px; border-left:4px solid transparent; }
.tz .ln .fl{ width:20px; flex:none; text-align:center; font-size:11px; color:transparent; }
.tz .ln .no{ width:2.4ch; flex:none; text-align:right; color:var(--filete); margin-right:12px; }
.tz .ln.hecha{ border-left-color:var(--acento); background:var(--suave); }
.tz .ln.hecha .fl{ color:var(--acento); }
.tz .ln.sig .fl{ color:var(--filete); }
.tz .kw{ color:var(--acento); font-weight:600; }
.tz .str{ color:#4A5A2A; }
.tz .num{ color:#1E4A6B; }
.tz-leyenda{ font-size:12.5px; color:var(--banda); display:flex; gap:12px; }
.tz-leyenda b{ color:var(--acento); }
.tz-narr{ min-height:4.4em; padding:10px 12px; background:var(--suave); border-left:4px solid var(--acento); font-size:15px; }
.tz-narr code{ font:500 13px/1 var(--mono); background:#fff; padding:2px 5px; border-radius:4px; }

.tz-mem{ padding:12px; display:flex; flex-direction:column; gap:16px; }
.tz-lnom{ font:600 14px/1 var(--mono); }
.tz-nota{ font:400 12px/1 var(--texto); color:var(--banda); }
.tz-casillas{ display:flex; position:relative; padding-top:44px; overflow-x:auto; }
.tz .cas{ display:flex; flex-direction:column; align-items:center; gap:5px; flex:none; }
.tz .cas .v{ width:50px; height:50px; border:2px solid var(--tinta); margin-left:-2px; display:flex; align-items:center; justify-content:center; font:600 19px/1 var(--mono); background:#fff; transition:background .25s,border-color .25s; }
.tz .cas:first-child .v{ margin-left:0; }
.tz .cas .idx{ font:500 12px/1 var(--mono); color:var(--banda); }
.tz .cas.visitada .v{ background:var(--fondo); color:var(--banda); }
.tz .cas.foco .v{ border:3px solid var(--acento); background:var(--suave); color:var(--tinta); position:relative; z-index:1; }
.tz .cas.lee .v{ box-shadow:0 0 0 5px rgba(122,31,54,.18); }
.tz .cas.foco .idx{ color:var(--acento); font-weight:600; }
.tz .puntero{ position:absolute; top:0; left:0; display:flex; flex-direction:column; align-items:center; gap:2px; transition:transform .35s ease; pointer-events:none; }
.tz .puntero .et{ font:600 13px/1 var(--mono); color:#fff; background:var(--acento); padding:5px 8px; border-radius:4px; white-space:nowrap; }
.tz .puntero .flecha{ width:0; height:0; border-left:7px solid transparent; border-right:7px solid transparent; border-top:9px solid var(--acento); }
.tz-consulta{ font:500 14px/1.3 var(--mono); color:var(--acento); min-height:1.3em; margin-top:6px !important; }
.tz-vars{ display:flex; flex-wrap:wrap; gap:8px; }
.tz .var{ border:1.5px solid var(--fila); border-radius:6px; padding:7px 11px; min-width:72px; display:flex; flex-direction:column; gap:2px; }
.tz .var .k{ font:500 12px/1 var(--mono); color:var(--banda); }
.tz .var .val{ font:600 19px/1.15 var(--mono); }
.tz .var.cambia{ border:2px solid var(--acento); background:var(--suave); }
.tz .var .antes{ font:400 11px/1 var(--mono); color:var(--banda); text-decoration:line-through; }
.tz-vacio{ font-size:14px; color:var(--banda); font-style:italic; }
.tz .cond{ border:1.5px dashed var(--filete); border-radius:8px; padding:10px 12px; display:flex; flex-direction:column; gap:5px; font:500 15px/1.35 var(--mono); }
.tz .cond .fila-c{ display:flex; gap:8px; align-items:center; flex-wrap:wrap; }
.tz .cond .gris{ color:var(--banda); }
.tz .cond .res{ font:700 13px/1 var(--titulo); padding:5px 9px; border-radius:999px; color:#fff; }
.tz .cond .res.si{ background:var(--si); }
.tz .cond .res.no{ background:var(--acento); }
.tz .cond .res.oculto{ background:var(--banda); }
.tz-consola{ background:var(--tinta); color:#EDEDED; font:400 14px/1.6 var(--mono); padding:10px 12px; min-height:2.6em; white-space:pre-wrap; }
.tz-consola .pr{ color:#9A9A9A; }

.tz-tabla-wrap{ overflow-x:auto; padding:12px 12px 0; }
table.tz-tabla{ width:100%; border-collapse:collapse; font:500 15px/1.2 var(--mono); margin:0; }
table.tz-tabla th{ font:600 11px/1.2 var(--titulo); letter-spacing:.06em; color:#fff; background:var(--tinta); padding:8px 10px; text-align:left; border:0; }
table.tz-tabla td{ padding:8px 10px; border:0; border-bottom:1px solid var(--fila); }
table.tz-tabla tr.nueva td{ background:var(--suave); }
table.tz-tabla tr.nueva td:first-child{ box-shadow:inset 4px 0 0 var(--acento); }
table.tz-tabla td.si{ color:var(--si); font-weight:600; }
table.tz-tabla td.no{ color:var(--acento); font-weight:600; }
table.tz-tabla tr.fantasma td{ color:var(--fila); }
.tz-nota-tabla{ font-size:13px; color:var(--banda); padding:8px 12px 12px; }

.tz-mandos{ display:flex; gap:8px; align-items:center; flex-wrap:wrap; border-top:1px solid var(--fila); padding-top:12px; }
.tz-b{ font:600 14px/1 var(--titulo); color:var(--tinta); background:#fff; border:1px solid var(--tinta); border-radius:999px; padding:10px 15px; cursor:pointer; }
.tz-b:hover{ background:var(--suave); }
.tz-b.prim{ background:var(--acento); border-color:var(--acento); color:#fff; }
.tz-b.prim:hover{ background:var(--oscuro); }
.tz-b:disabled{ opacity:.35; cursor:default; }
.tz-b:focus-visible,.tz-pred:focus-visible{ outline:2px solid var(--acento); outline-offset:2px; }
.tz-cuenta{ font:500 13px/1 var(--mono); color:var(--banda); }
.tz-toggle{ display:flex; gap:7px; align-items:center; font-size:14px; color:var(--sub); cursor:pointer; margin-left:auto; }
.tz-toggle input{ accent-color:var(--acento); width:17px; height:17px; }

@media (max-width:760px){
  .tz{ padding:12px; }
  .tz-escena{ grid-template-columns:1fr; }
  .tz .cas .v{ width:44px; height:44px; font-size:17px; }
  .tz-toggle{ margin-left:0; width:100%; }
}
@media (prefers-reduced-motion:reduce){ .tz *{ transition:none !important; } }
`;

const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
const fmtVal = v => (typeof v === "string" ? '"' + v + '"' : String(v));
const igual = (a, b) => JSON.stringify(a) === JSON.stringify(b);

function colorea(linea) {
  return esc(linea).split(/("[^"]*")/).map(p => p.startsWith('"')
    ? '<span class="str">' + p + "</span>"
    : p.replace(/\b(for|in|while|if|elif|else|and|or|not|print|range|len|def|return)\b/g, '<span class="kw">$1</span>')
       .replace(/\b(\d+)\b/g, '<span class="num">$1</span>')).join("");
}

const PLANTILLA = `
<div class="tz">
  <div class="tz-cab"><span class="tz-tit"></span><span class="tz-etq"></span></div>
  <p class="tz-idea"></p>
  <div class="tz-escena">
    <div class="tz-col">
      <div class="tz-caja">
        <div class="tz-barra"><span>Programa</span><span class="tz-linea">listo</span></div>
        <pre class="tz-codigo" aria-label="Código del programa"></pre>
      </div>
      <p class="tz-leyenda"><b>▶</b> se acaba de ejecutar <span>▷ la siguiente</span></p>
      <p class="tz-narr" aria-live="polite"></p>
    </div>
    <div class="tz-col">
      <div class="tz-caja">
        <div class="tz-barra negro"><span>Memoria</span><span>lo que hay ahora</span></div>
        <div class="tz-mem">
          <div>
            <p class="tz-lnom"><span class="tz-nom"></span> <span class="tz-nota">(posiciones desde 0)</span></p>
            <div class="tz-casillas"></div>
            <p class="tz-consulta"></p>
          </div>
          <div><p class="tz-micro">Variables</p><div class="tz-vars"></div></div>
          <div class="tz-cond"></div>
        </div>
      </div>
      <div><p class="tz-micro">Pantalla</p><div class="tz-consola" aria-live="polite"></div></div>
    </div>
  </div>
  <div class="tz-caja">
    <div class="tz-barra"><span>Tabla de traza</span><span>una fila por vuelta</span></div>
    <div class="tz-tabla-wrap"><table class="tz-tabla"></table></div>
    <p class="tz-nota-tabla"></p>
  </div>
  <div class="tz-mandos">
    <button type="button" class="tz-b tz-atras" aria-label="Paso anterior">◀</button>
    <button type="button" class="tz-b prim tz-sigue">Paso ▶</button>
    <button type="button" class="tz-b tz-play">Reproducir</button>
    <button type="button" class="tz-b tz-reinicia">Reiniciar</button>
    <span class="tz-cuenta"></span>
    <label class="tz-toggle"><input type="checkbox" class="tz-pred"> Modo predicción</label>
  </div>
</div>`;

function render({ model, el }) {
  const C = model.get("config") || {};
  const D = model.get("traza");
  if (!D || !D.pasos) { el.textContent = "Falta la traza: ejecuta herramientas/trazar.py sobre este capítulo."; return; }
  el.innerHTML = "<style>" + ESTILOS + "</style>" + PLANTILLA;
  const q = s => el.querySelector(s);
  const P = D.pasos, L = D.codigo.split("\n"), lista = C.lista, cab = C.cabecera;
  const columnas = C.columnas.concat(C.fila_en === "comprobacion" ? ["¿sigue?"] : []);
  let k = 0, oculto = false, timer = null;

  q(".tz-tit").textContent = C.titulo || "";
  q(".tz-etq").textContent = C.etiqueta || "";
  q(".tz-idea").textContent = C.idea || "";
  q(".tz-nom").textContent = lista;
  q(".tz-nota-tabla").textContent = C.fila_en === "comprobacion"
    ? "En el while, la fila se escribe cada vez que se comprueba la condición."
    : "La fila de cada vuelta se escribe al terminarla, cuando el for vuelve a la cabecera.";

  const salida = t => t.split("\n").filter(Boolean);
  const saleDelBucle = (p, sig) => p.linea === cab && !p.cond && (!sig || sig.linea !== cab + 1);

  function narra(p, prev, sig) {
    if (p.linea === null) return "El programa está listo. Pulsa «Paso» para ejecutar la primera línea.";
    const txt = L[p.linea - 1].trim();
    const cambios = Object.keys(p.estado).filter(n => n !== lista && !igual(p.estado[n], prev.estado[n]));
    if (!(lista in prev.estado) && (lista in p.estado))
      return "Se crea la lista <code>" + lista + "</code> con " + p.estado[lista].length + " casillas, numeradas de 0 a " + (p.estado[lista].length - 1) + ".";
    if (p.cond) {
      const r = p.cond.valor;
      if (txt.startsWith("while")) return "Se comprueba la condición del <code>while</code>: " + (r ? "es <b>True</b>, así que da otra vuelta." : "es <b>False</b>, así que sale del bucle.");
      return "Se evalúa la condición del <code>if</code>: " + (r ? "es <b>True</b>, así que entra en el bloque." : "es <b>False</b>, así que se salta el bloque.");
    }
    if (p.linea === cab) {
      if (saleDelBucle(p, sig)) return "No quedan " + (txt.includes("range") ? "posiciones" : "elementos") + " por recorrer: el bucle <code>for</code> termina.";
      if (txt.includes("range")) return "Vuelta " + p.vuelta + ": <code>" + C.puntero + "</code> pasa a valer " + p.estado[C.puntero] + ". Es la siguiente posición que se va a consultar.";
      return "Vuelta " + p.vuelta + ": Python toma el siguiente elemento, el de la posición " + p.foco + ", y lo guarda en <code>" + C.puntero + "</code> = " + fmtVal(p.estado[C.puntero]) + ".";
    }
    if (txt.startsWith("print")) return "Se muestra en pantalla: <code>" + esc(salida(p.salida).slice(-1)[0] || "") + "</code>";
    if (cambios.length) {
      const n = cambios[0], a = prev.estado[n];
      const lee = p.lee && p.foco !== null ? " Para ello se consulta la casilla " + p.foco + " de la lista, que vale " + fmtVal(p.estado[lista][p.foco]) + "." : "";
      if (a === undefined) return "Se crea la variable <code>" + n + "</code> y vale " + fmtVal(p.estado[n]) + "." + lee;
      return "<code>" + n + "</code> cambia: valía " + fmtVal(a) + " y ahora vale " + fmtVal(p.estado[n]) + "." + lee;
    }
    return "Se ejecuta la línea " + p.linea + ".";
  }

  function pinta() {
    const p = P[k], prev = P[Math.max(0, k - 1)], sig = P[k + 1];
    q(".tz-linea").textContent = p.linea === null ? "listo" : "línea " + p.linea;

    q(".tz-codigo").innerHTML = L.map((l, i) => {
      const n = i + 1, hecha = p.linea === n, s = sig && sig.linea === n && !hecha;
      return '<div class="ln' + (hecha ? " hecha" : "") + (s ? " sig" : "") + '"><span class="fl">' + (hecha ? "▶" : "▷") +
        '</span><span class="no">' + n + "</span><span>" + colorea(l) + "</span></div>";
    }).join("");

    const arr = p.estado[lista];
    const foco = saleDelBucle(p, sig) ? null : p.foco;
    const cas = q(".tz-casillas");
    if (!arr) { cas.innerHTML = '<span class="tz-vacio">Todavía no existe: se crea en la línea 1.</span>'; q(".tz-consulta").textContent = ""; }
    else {
      let h = "";
      arr.forEach((v, i) => {
        h += '<div class="cas' + (i === foco ? " foco" : "") + (foco !== null && i < foco ? " visitada" : "") + (i === foco && p.lee ? " lee" : "") +
          '"><span class="v">' + esc(fmtVal(v)) + '</span><span class="idx">' + i + "</span></div>";
      });
      if (foco !== null) h += '<div class="puntero"><span class="et">' + (C.puntero === "i" || /range/.test(L[cab - 1]) ? C.puntero + " = " + p.estado[C.puntero] : C.puntero) + '</span><span class="flecha"></span></div>';
      cas.innerHTML = h;
      if (foco !== null) {
        const c = cas.children[foco], pu = cas.querySelector(".puntero");
        requestAnimationFrame(() => { pu.style.transform = "translateX(" + (c.offsetLeft + c.offsetWidth / 2 - pu.offsetWidth / 2) + "px)"; });
      }
      q(".tz-consulta").textContent = (p.lee && foco !== null) ? "Se consulta " + lista + "[" + foco + "] → " + (oculto ? "?" : fmtVal(arr[foco])) : "";
    }

    const nombres = Object.keys(p.estado).filter(n => n !== lista);
    q(".tz-vars").innerHTML = nombres.length ? nombres.map(n => {
      const cambia = k > 0 && !igual(p.estado[n], prev.estado[n]);
      const antes = cambia && prev.estado[n] !== undefined ? '<span class="antes">' + esc(fmtVal(prev.estado[n])) + "</span>" : "";
      return '<div class="var' + (cambia ? " cambia" : "") + '"><span class="k">' + n + '</span><span class="val">' +
        (oculto && cambia ? "?" : esc(fmtVal(p.estado[n]))) + "</span>" + antes + "</div>";
    }).join("") : '<span class="tz-vacio">Aún no hay variables.</span>';

    if (p.cond) {
      const r = p.cond.valor;
      q(".tz-cond").innerHTML = '<div class="cond"><span class="tz-micro acento">Condición</span><div>' + esc(p.cond.expr) +
        '</div><div class="fila-c"><span class="gris">→</span><span>' + esc(p.cond.sust) + '</span><span class="gris">→</span><span class="res ' +
        (oculto ? "oculto" : (r ? "si" : "no")) + '">' + (oculto ? "¿True o False?" : (r ? "True" : "False")) + "</span></div></div>";
    } else q(".tz-cond").innerHTML = "";

    const out = salida(p.salida), nueva = p.salida !== prev.salida;
    q(".tz-consola").innerHTML = out.length
      ? out.map((l, i) => '<span class="pr">&gt;&gt;&gt; </span>' + esc(oculto && nueva && i === out.length - 1 ? "?" : l)).join("\n")
      : '<span class="pr">(nada todavía)</span>';

    const vis = P.slice(0, k + 1).filter(x => x.fila !== null && x.fila !== undefined).map(x => x.fila);
    let t = "<thead><tr><th>" + (C.fila_en === "comprobacion" ? "Comprobación" : "Vuelta") + "</th>" + columnas.map(c => "<th>" + esc(c) + "</th>").join("") + "</tr></thead><tbody>";
    D.filas.forEach((f, i) => {
      const v = vis.includes(i), nv = v && p.fila === i;
      t += '<tr class="' + (nv ? "nueva" : "") + (v ? "" : " fantasma") + '"><td>' + (i + 1) + "</td>" + f.map(c => {
        if (!v) return "<td>·</td>";
        const cls = oculto && nv ? "" : (c === "Sí" ? "si" : c === "No" ? "no" : "");
        return '<td class="' + cls + '">' + esc(oculto && nv ? "?" : c) + "</td>";
      }).join("") + "</tr>";
    });
    q(".tz-tabla").innerHTML = t + "</tbody>";

    q(".tz-narr").innerHTML = oculto ? "<b>Predice antes de mirar.</b> ¿Qué valor saldrá donde ves «?»? Piénsalo y pulsa «Revelar»." : narra(p, prev, sig);
    q(".tz-cuenta").textContent = k + " / " + (P.length - 1);
    q(".tz-atras").disabled = k === 0;
    const fin = k === P.length - 1 && !oculto;
    q(".tz-sigue").disabled = fin;
    q(".tz-sigue").textContent = oculto ? "Revelar" : "Paso ▶";
    if (fin) para();
  }

  function avanza() {
    if (oculto) { oculto = false; pinta(); return; }
    if (k < P.length - 1) {
      k++;
      const p = P[k], prev = P[k - 1];
      const novedad = p.cond || (p.fila !== null && p.fila !== undefined) || p.salida !== prev.salida ||
        Object.keys(p.estado).some(n => n !== lista && !igual(p.estado[n], prev.estado[n]));
      oculto = q(".tz-pred").checked && !!novedad;
      pinta();
    }
  }
  function para() { if (timer) { clearInterval(timer); timer = null; } q(".tz-play").textContent = "Reproducir"; }

  q(".tz-sigue").addEventListener("click", () => { para(); avanza(); });
  q(".tz-atras").addEventListener("click", () => { para(); oculto = false; if (k > 0) k--; pinta(); });
  q(".tz-reinicia").addEventListener("click", () => { para(); oculto = false; k = 0; pinta(); });
  q(".tz-pred").addEventListener("change", () => { oculto = false; pinta(); });
  q(".tz-play").addEventListener("click", () => {
    if (timer) { para(); return; }
    if (k === P.length - 1) { k = 0; oculto = false; }
    q(".tz-play").textContent = "Pausa";
    timer = setInterval(() => { avanza(); if (oculto) para(); }, 1100);
  });
  const alRedimensionar = () => pinta();
  window.addEventListener("resize", alRedimensionar);
  pinta();
  return () => { para(); window.removeEventListener("resize", alRedimensionar); };
}

export default { render };
