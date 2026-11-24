// ── Diagrama de flujo ───────────────────────────────────────────────────────────────────────
// Pieza común del libro (widgets/traza.mjs, que lo carga de <web>/datos/diagrama.js) y del
// laboratorio «Mirar y ver» (se inyecta en su página). Los bloques los da herramientas/diagrama.py;
// aquí se maquetan como bloques anidados (sin librería de grafos) y, en cada paso, se ilumina el
// bloque de la línea que toca.
//   const d = DG.crea(datos);  el.innerHTML = d.html;  d.conecta(el);  d.pinta(el, pasos, k, opciones)
//   pasos: [{l: línea}], opciones.hecha: la línea del paso k ya se ha ejecutado (libro) o va a ejecutarse (Mirar y ver)
// Colores y letra salen de variables CSS que pone cada página en el contenedor .dgc:
//   --dg-tinta --dg-sub --dg-mut --dg-fondo --dg-suave --dg-acento --dg-acento-f --dg-banda --dg-mono --dg-titulo --dg-texto
const DG = (() => {
  const CW = 7.2, RH = 20, PX = 12, BADGE = 26, GV = 22;
  const NOTA = {ret:'termina la función', brk:'sale del bucle', cont:'vuelve al bucle', raise:'lanza el error'};
  const tw = s => s.length * CW;
  const E = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  const camino = pts => 'M' + pts.map(p => p.join(',')).join(' L');
  const ar = (pts, cls='', extra='') => `<path class="de ${cls}" ${extra} d="${camino(pts)}" marker-end="url(#dg-fl)"/>`;
  const ln = (pts, cls='', extra='') => `<path class="de ${cls}" ${extra} d="${camino(pts)}"/>`;
  const lab = (x, y, t, id, r, anchor='start') => `<text class="dl" x="${x}" y="${y}" text-anchor="${anchor}" data-id="${id}" data-r="${r}">${t}</text>`;
  const lineas = seq => { const S = new Set(); const add = b => { if (b.r) b.r.forEach(([a,c]) => { for (let i=a;i<=c;i++) S.add(i); });
      if (b.l) for (let i=b.l[0]; i<=b.l[1]; i++) S.add(i);
      ['si','no','b','els','fin'].forEach(k => (b[k]||[]).forEach(add)); (b.h||[]).forEach(h => { for (let i=h.l[0];i<=h.l[1];i++) S.add(i); h.b.forEach(add); }); };
    seq.forEach(add); return S; };

  const CSS = `
.dgc .dgf{margin:0;flex:none;max-width:100%}.dgc figcaption{font:600 11px var(--dg-titulo);letter-spacing:.08em;text-transform:uppercase;color:var(--dg-mut);margin:0 0 6px}
.dgc .dgf svg{display:block;max-width:100%;height:auto;overflow:visible}
.dgc .ds{fill:var(--dg-fondo);stroke:var(--dg-tinta);stroke-width:1.3}.dgc .kd .ds{fill:var(--dg-suave)}
.dgc .ko .ds{fill:var(--dg-banda);stroke:var(--dg-banda)}.dgc .ko .dk,.dgc .ko .dt{fill:#fff}
.dgc .dt{font:12px var(--dg-mono);fill:var(--dg-tinta)}.dgc .dk{font:600 11px var(--dg-titulo);fill:var(--dg-sub)}
.dgc .dn2{font:italic 10.5px var(--dg-texto);fill:var(--dg-mut)}
.dgc .dc{font:600 10.5px var(--dg-titulo);fill:var(--dg-mut)}
.dgc .hl{fill:transparent}.dgc .dfr{fill:none;stroke:var(--dg-mut);stroke-dasharray:5 4}
.dgc .de{fill:none;stroke:var(--dg-mut);stroke-width:1.3}.dgc .de.dsh{stroke-dasharray:4 3}.dgc .dar{fill:var(--dg-mut)}.dgc .dm{fill:var(--dg-mut)}
.dgc .de.dj{stroke-dasharray:5 3}
.dgc .dl{font:600 10.5px var(--dg-titulo);fill:var(--dg-mut)}
.dgc .de.on{stroke:var(--dg-acento);stroke-width:2.6}.dgc .dl.on{fill:var(--dg-acento)}
.dgc .dn.act .hl,.dgc .dn.act .hl2{fill:var(--dg-suave)}.dgc .dn.act .dt{font-weight:600}.dgc .dn.act .ds{stroke:var(--dg-acento);stroke-width:2.4}
.dgc .kp .dn.act .hl,.dgc .kio .dn.act .hl{stroke:var(--dg-acento);stroke-width:2}
.dgc .ko.act .ds{fill:var(--dg-acento-f);stroke:var(--dg-acento-f)}
.dgc .dn.act .dc{fill:var(--dg-acento)}
.dgc .dn.sig .hl,.dgc .dn.sig .hl2{stroke:var(--dg-acento);stroke-width:1.2;stroke-dasharray:3 2}.dgc .dn.prev .dt{fill:var(--dg-sub)}
.dgc .dn.never .dt{fill:var(--dg-mut);opacity:.55}
.dgc .dn.act .dfr{stroke:var(--dg-acento);stroke-width:2;fill:var(--dg-suave);fill-opacity:.35}.dgc .dn.act > .dk{fill:var(--dg-acento)}
.dgc .dge{color:#A1252C;font-size:14px;margin:0}`;

  function crea(D){
    let uid = 0, bucles = [];
    const heads = [];

    function caja(b){          // proceso o entrada/salida: una fila por sentencia
      const io = b.t==='io', sk = io ? 10 : 0, w = Math.max(...b.r.map(r => tw(r[2]))) + 2*PX + BADGE + 2*sk, h = b.r.length*RH + 10;
      const forma = io ? `<polygon class="ds" points="${sk},0 ${w},0 ${w-sk},${h} 0,${h}"/>` : `<rect class="ds" x="0" y="0" width="${w}" height="${h}"/>`;
      const filas = b.r.map(([a,c,t],i) => `<g class="dn" data-a="${a}" data-b="${c}"><rect class="hl" x="${sk+3}" y="${5+i*RH}" width="${w-2*sk-6}" height="${RH}"/><text class="dt" x="${(w-BADGE)/2}" y="${5+i*RH+14}" text-anchor="middle">${E(t)}</text><text class="dc" x="${w-sk-6}" y="${5+i*RH+14}" text-anchor="end"></text></g>`).join('');
      return {w, h, cx:w/2, term:false, svg:`<g class="${io?'kio':'kp'}">${forma}${filas}</g>`};
    }
    function fin(b){           // return, break, continue, raise: el camino termina aquí
      const w = Math.max(tw(b.x), NOTA[b.k].length*6.2) + 34, h = 40;
      const salta = (b.k==='brk' || b.k==='cont') && bucles.length ? ` data-salto="${b.k}" data-bucle="${bucles[bucles.length-1]}"` : '';
      return {w, h, cx:w/2, term:true, svg:`<g class="dn kf" data-a="${b.l[0]}" data-b="${b.l[1]}"${salta} data-w="${w}" data-h="${h}"><rect class="ds hl2" x="0" y="0" width="${w}" height="${h}" rx="${h/2}"/><text class="dt" x="${w/2}" y="17" text-anchor="middle">${E(b.x)}</text><text class="dn2" x="${w/2}" y="32" text-anchor="middle">${NOTA[b.k]}</text><text class="dc" x="${w+4}" y="12"></text></g>`};
    }
    function rombo(c, l){      // condición
      const dw = Math.max(tw(c) + 50, 96), dh = 46;
      return {dw, dh, svg:(x) => `<g class="dn kd" data-a="${l[0]}" data-b="${l[1]}"><polygon class="ds hl2" points="${x},0 ${x+dw/2},${dh/2} ${x},${dh} ${x-dw/2},${dh/2}"/><text class="dt" x="${x}" y="${dh/2+4}" text-anchor="middle">${E(c)}</text><text class="dc" x="${x-dw/2+2}" y="11"></text></g>`};
    }
    function hexa(c, l){       // cabecera del for
      const t = 'for ' + c, dw = tw(t) + 44, dh = 40;
      return {dw, dh, svg:(x) => `<g class="dn kd" data-a="${l[0]}" data-b="${l[1]}"><polygon class="ds hl2" points="${x-dw/2+14},0 ${x+dw/2-14},0 ${x+dw/2},${dh/2} ${x+dw/2-14},${dh} ${x-dw/2+14},${dh} ${x-dw/2},${dh/2}"/><text class="dt" x="${x}" y="${dh/2+4}" text-anchor="middle">${E(t)}</text><text class="dc" x="${x-dw/2+10}" y="-4"></text></g>`};
    }
    function si(b){            // if: Sí baja por el eje; No sale a la derecha
      const S = seq(b.si), N = seq(b.no), R = rombo(b.c, b.l), id = uid++;
      heads.push({id, kind:'if', a:b.l[0], z:b.l[1], si:lineas(b.si)});
      const cx = Math.max(S.empty ? 0 : S.cx, R.dw/2) + 2, top = R.dh + GV;
      const r1 = Math.max(cx + (S.empty ? 0 : S.w - S.cx), cx + R.dw/2);
      const xr = N.empty ? r1 + 18 : r1 + 30 + N.cx;
      const hS = S.empty ? 0 : S.h, hN = N.empty ? 0 : N.h, m = top + Math.max(hS, hN) + 18;
      let g = R.svg(cx);
      g += ar([[cx,R.dh],[cx,top]], 'r-si', `data-id="${id}" data-r="si"`) + lab(cx+6, R.dh+13, 'Sí', id, 'si');
      if (!S.empty) g += `<g transform="translate(${cx-S.cx},${top})">${S.svg}</g>`;
      const nTop = N.empty ? m : top;
      g += (N.empty ? ln : ar)([[cx+R.dw/2,R.dh/2],[xr,R.dh/2],[xr,nTop]], 'r-no', `data-id="${id}" data-r="no"`) + lab(cx+R.dw/2+6, R.dh/2-6, 'No', id, 'no');
      if (!N.empty) g += `<g transform="translate(${xr-N.cx},${top})">${N.svg}</g>`;
      const term = !S.empty && !N.empty && S.term && N.term;
      if (!term){
        if (!S.term) g += ln([[cx, top+hS],[cx, m]]);
        if (N.empty || !N.term) g += ln([[xr, N.empty ? m : top+hN],[xr, m],[cx+5, m]]);
        g += `<circle class="dm" cx="${cx}" cy="${m}" r="3.5"/>`;
      }
      const w = N.empty ? xr + 10 : xr - N.cx + N.w + 2;
      return {w, h: term ? top + Math.max(hS, hN) : m, cx, term, svg:g};
    }
    function bucle(b){         // while y for: el cuerpo en el eje, la vuelta por la izquierda, la salida por la derecha
      const id = uid++;
      bucles.push(id); const B = seq(b.b); bucles.pop();
      const H = b.t==='for' ? hexa(b.c, b.l) : rombo(b.c, b.l);
      heads.push({id, kind:b.t, a:b.l[0], z:b.l[1], si:lineas(b.b)});
      const half = Math.max(B.empty ? 0 : B.cx, H.dw/2), cx = half + 22, top = H.dh + GV;
      const hB = B.empty ? 0 : B.h, yb = top + hB, xL = cx - half - 16;
      const xR = Math.max(cx + (B.empty ? 0 : B.w - B.cx), cx + H.dw/2) + 20, yE = yb + 30;
      const [tsi, tno] = b.t==='for' ? ['siguiente', 'terminado'] : ['Sí', 'No'];
      let g = H.svg(cx);
      g += ar([[cx,H.dh],[cx,top]], 'r-si', `data-id="${id}" data-r="si"`) + lab(cx+6, H.dh+13, tsi, id, 'si');
      if (!B.empty) g += `<g transform="translate(${cx-B.cx},${top})">${B.svg}</g>`;
      // si el cuerpo acaba en break/return no baja nada por el eje, pero un continue puede usar el carril de la vuelta
      const cont = B.svg.includes(`data-salto="cont" data-bucle="${id}"`);
      if (!B.term || cont) g += ar([...(B.term ? [] : [[cx,yb],[cx,yb+12]]), [xL,yb+12],[xL,H.dh/2],[cx-H.dw/2,H.dh/2]], 'r-vu', `data-id="${id}" data-r="vu"`) + lab(xL+4, yb+24, 'otra vuelta', id, 'vu');
      g += ar([[cx+H.dw/2,H.dh/2],[xR,H.dh/2],[xR,yE],[cx+5,yE]], 'r-no', `data-id="${id}" data-r="no"`) + lab(cx+H.dw/2+6, H.dh/2-6, tno, id, 'no');
      g += `<circle class="dm" cx="${cx}" cy="${yE}" r="3.5"/>`;
      // puntos de llegada de break (carril de salida) y continue (carril de la vuelta)
      g += `<g class="dga" data-bucle="${id}" data-xs="${xR}" data-xv="${xL}" data-y0="${H.dh/2}" data-y1="${yb+12}"></g>`;
      return {w: xR + 8, h: yE, cx, term:false, svg:g};
    }
    function intento(b){       // try: el cuerpo en un marco; cada except, en otro a la derecha
      const T = seq(b.b), Hs = b.h.map(h => ({h, S:seq(h.b)})), pad = 12, ht = 22;
      const fw = Math.max(T.empty ? 60 : T.w, 60) + 2*pad, fh = ht + (T.empty ? 20 : T.h) + pad, cx = fw/2;
      let g = `<g class="dn kt" data-a="${b.l[0]}" data-b="${b.l[1]}"><rect class="dfr hl2" x="0" y="0" width="${fw}" height="${fh}"/><text class="dk" x="8" y="15">try</text><text class="dc" x="${fw-6}" y="15" text-anchor="end"></text></g><g>`;
      if (!T.empty) g += `<g transform="translate(${cx-T.cx},${ht})">${T.svg}</g>`;
      g += '</g>';
      let x = fw + 34, hmax = fh; const sal = [];
      Hs.forEach(({h, S}) => {
        const w = Math.max(S.empty ? 60 : S.w, tw(h.x) + 16) + 2*pad, hh = ht + (S.empty ? 20 : S.h) + pad;
        g += ln([[fw, 11],[x, 11]], 'dsh') + `<text class="dl" x="${fw+4}" y="-4">si hay error</text>`;
        g += `<g class="dn kx" data-a="${h.l[0]}" data-b="${h.l[1]}"><rect class="dfr hl2" x="${x}" y="0" width="${w}" height="${hh}"/><text class="dk" x="${x+8}" y="15">${E(h.x)}</text><text class="dc" x="${x+w-6}" y="15" text-anchor="end"></text></g>`;
        if (!S.empty) g += `<g transform="translate(${x+w/2-S.cx},${ht})">${S.svg}</g>`;
        if (!S.term) sal.push([x + w/2, hh]);
        hmax = Math.max(hmax, hh); x += w + 20;
      });
      const m = hmax + 16;
      g += ln([[cx, fh],[cx, m]]);
      sal.forEach(([sx, sy]) => g += ln([[sx, sy],[sx, m],[cx+5, m]]));
      g += `<circle class="dm" cx="${cx}" cy="${m}" r="3.5"/>`;
      const extra = seq([...(b.els||[]), ...(b.fin||[])]);
      if (!extra.empty){ g += ar([[cx,m],[cx,m+GV]]) + `<g transform="translate(${cx-extra.cx},${m+GV})">${extra.svg}</g>`; }
      return {w: Math.max(x - 20, extra.empty ? 0 : cx - extra.cx + extra.w), h: extra.empty ? m : m + GV + extra.h, cx, term: !extra.empty && extra.term, svg:g};
    }
    function bloque(b){
      if (b.t==='p' || b.t==='io') return caja(b);
      if (b.t==='fin') return fin(b);
      if (b.t==='if') return si(b);
      if (b.t==='wh' || b.t==='for'){ const L = bucle(b); return (b.els && b.els.length) ? seq([{t:'__', L}, ...b.els]) : L; }
      if (b.t==='try') return intento(b);
      if (b.t==='__') return b.L;
      return caja({t:'p', r:[[0,0,'?']]});
    }
    function seq(list){
      if (!list || !list.length) return {w:0, h:0, cx:0, term:false, empty:true, svg:''};
      const L = list.map(bloque), cx = Math.max(...L.map(x => x.cx));
      let y = 0, g = '', w = 0, term = false;
      L.forEach((x, i) => {
        if (i){ if (!L[i-1].term) g += ar([[cx,y],[cx,y+GV]]); y += GV; }
        g += `<g transform="translate(${cx-x.cx},${y})">${x.svg}</g>`;
        y += x.h; w = Math.max(w, cx - x.cx + x.w); term = x.term;
      });
      return {w, h:y, cx, term, svg:g};
    }
    function ovalo(t, sub, a){
      const w = Math.max(tw(t) + 40, 90), h = 32;
      return {w, h, cx:w/2, svg:`<g class="dn ko"${a!==undefined ? ` data-a="${a}" data-b="${a}"` : ''}><rect class="ds hl2" x="0" y="0" width="${w}" height="${h}" rx="16"/><text class="${sub?'dt':'dk'}" x="${w/2}" y="20" text-anchor="middle">${E(t)}</text></g>`};
    }
    function diagrama(titulo, cuerpo, ini, finT){
      bucles = [];
      const S = seq(cuerpo), A = ovalo(ini.t, ini.code), Z = S.term ? null : ovalo(finT.t, false, finT.a);
      const cx = Math.max(S.cx, A.cx, Z ? Z.cx : 0) + 8;
      let y = 0, g = `<g transform="translate(${cx-A.cx},0)">${A.svg}</g>`; y = A.h;
      if (!S.empty){ g += ar([[cx,y],[cx,y+GV]]); y += GV; g += `<g transform="translate(${cx-S.cx},${y})">${S.svg}</g>`; y += S.h; }
      if (Z){ g += ar([[cx,y],[cx,y+GV]]); y += GV; g += `<g transform="translate(${cx-Z.cx},${y})">${Z.svg}</g>`; y += Z.h; }
      const W = Math.ceil(Math.max(cx + Math.max(S.empty?0:S.w-S.cx, A.w/2, Z?Z.w/2:0), cx + 40) + 34), H = Math.ceil(y + 6);
      return `<figure class="dgf"><figcaption>${E(titulo)}</figcaption><svg viewBox="-4 -4 ${W+8} ${H+8}" width="${W+8}" style="min-width:${Math.round((W+8)*.72)}px" role="img" aria-label="Diagrama de flujo: ${E(titulo)}">${g}<g class="dsaltos"></g></svg></figure>`;
    }

    let html;
    if (!D) html = '';
    else if (D.error) html = `<p class="dge">No se puede dibujar el diagrama: ${E(D.error)}</p>`;
    else {
      html = `<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><marker id="dg-fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="dar"/></marker></defs></svg>`;
      html += diagrama('Programa', D.main, {t:'Inicio'}, {t:'Fin', a:0});
      D.fn.forEach(f => html += diagrama('Función ' + f.n.split('.').pop(), f.b, {t:f.sig, code:true}, {t:'fin · devuelve None'}));
    }

    // posición de un elemento dentro de su svg: suma de los translate de sus antepasados
    const origen = el => { let x = 0, y = 0;
      for (let n = el; n && n.tagName && n.tagName.toLowerCase() !== 'svg'; n = n.parentNode){
        const m = /translate\(([-\d.]+)[ ,]+([-\d.]+)\)/.exec(n.getAttribute && n.getAttribute('transform') || '');
        if (m){ x += +m[1]; y += +m[2]; } }
      return [x, y]; };
    // flechas de break (hasta el carril de salida del bucle) y continue (hasta el carril de la vuelta)
    function conecta(el){
      el.querySelectorAll('svg').forEach(svg => {
        const capa = svg.querySelector('.dsaltos'); if (!capa) return;
        let h = '';
        svg.querySelectorAll('.kf[data-salto]').forEach(p => {
          const a = svg.querySelector(`.dga[data-bucle="${p.dataset.bucle}"]`); if (!a) return;
          const [px, py] = origen(p), [ax, ay] = origen(a), w = +p.dataset.w, hh = +p.dataset.h, y = py + hh/2;
          const brk = p.dataset.salto === 'brk';
          const xd = brk ? ax + +a.dataset.xs : ax + +a.dataset.xv, x0 = brk ? px + w : px;
          h += `<path class="de dj" data-a="${p.dataset.a}" data-b="${p.dataset.b}" d="${camino([[x0, y], [xd, y]])}" marker-end="url(#dg-fl)"/>`;
          if (brk) h += `<text class="dl" data-a="${p.dataset.a}" x="${x0 + 4}" y="${y - 4}">a la salida</text>`;
        });
        capa.innerHTML = h;
      });
    }

    // ilumina el paso k. Mirar y ver: la línea del paso k va a ejecutarse (y se marca la anterior).
    // Libro (hecha): la línea del paso k se acaba de ejecutar (y se marca la siguiente).
    function pinta(el, tr, k, op = {}){
      if (!el) return;
      const hecha = !!op.hecha, s = tr[k] || {}, p = k ? tr[k-1] : null, n1 = tr[k+1], last = k===tr.length-1, hasta = new Map();
      for (let j=0; j<(hecha ? k+1 : k); j++) if (tr[j].l) hasta.set(tr[j].l, (hasta.get(tr[j].l)||0) + 1);
      const veces = (a, b) => { let n = 0; for (let i=a;i<=b;i++) n += hasta.get(i) || 0; return n; };
      const dentro = (n, a, b) => n!==null && n!==undefined && n>=a && n<=b;
      const otra = hecha ? (n1 ? n1.l : null) : (p ? p.l : null);
      let act = null;
      el.querySelectorAll('.dn').forEach(g => {
        if (g.dataset.a===undefined){ g.classList.remove('act','prev','sig','never'); return; }
        const a = +g.dataset.a, b = +g.dataset.b, on = s.l===0 && a===0 ? !hecha || last : dentro(s.l, a, b) && a!==0;
        const ot = !on && a!==0 && dentro(otra, a, b), n = a===0 ? 0 : veces(a, b);
        g.classList.toggle('act', !!on); g.classList.toggle(hecha ? 'sig' : 'prev', !!ot); g.classList.remove(hecha ? 'prev' : 'sig');
        g.classList.toggle('never', last && !on && a!==0 && !n);
        if (on && !act) act = g;
        const c = g.querySelector('.dc'); if (c) c.textContent = n ? '×' + n : '';
      });
      if (hecha && last && !act) { const f = el.querySelector('.ko[data-a="0"]'); if (f){ f.classList.add('act'); act = f; } }
      // ramas: por dónde salió cada condición hasta ahora, y cuál se acaba de tomar
      const cnt = {}; heads.forEach(H => cnt[H.id] = {si:0, no:0, vu:0});
      let tomada = null, salto = null;
      for (let j=1;j<=k;j++){
        const a = tr[j-1].l, b = tr[j].l;
        if (a==null) continue;
        for (const H of heads){
          if (a>=H.a && a<=H.z){ const r = H.si.has(b) ? 'si' : 'no'; cnt[H.id][r]++; if (j===k) tomada = [H.id, r]; }
          else if (H.kind!=='if' && b!=null && b>=H.a && b<=H.z && H.si.has(a)){ cnt[H.id].vu++; if (j===k) tomada = [H.id, 'vu']; }
        }
        if (j===k) salto = a;
      }
      el.querySelectorAll('.de[data-id]').forEach(e => e.classList.toggle('on', !!tomada && +e.dataset.id===tomada[0] && e.dataset.r===tomada[1]));
      el.querySelectorAll('.de.dj').forEach(e => e.classList.toggle('on', dentro(salto, +e.dataset.a, +e.dataset.b)));
      el.querySelectorAll('.dl[data-id]').forEach(t => {
        const c = cnt[t.dataset.id]; if (!c) return;
        if (!t.dataset.t) t.dataset.t = t.textContent;
        const n = c[t.dataset.r]; t.textContent = t.dataset.t + (n ? ' ×' + n : '');
        t.classList.toggle('on', !!tomada && +t.dataset.id===tomada[0] && t.dataset.r===tomada[1]);
      });
      el.querySelectorAll('.dsaltos .dl').forEach(t => t.classList.toggle('on', dentro(salto, +t.dataset.a, +t.dataset.a)));
      if (act && act.getBoundingClientRect){   // que el bloque activo quede a la vista dentro del panel, sin mover la página
        const r = act.getBoundingClientRect(), c = el.getBoundingClientRect();
        if (c.height && (r.top < c.top + 10 || r.bottom > c.bottom - 10)) el.scrollTop += (r.top - c.top) - c.height/3;
        if (c.width && (r.left < c.left || r.right > c.right)) el.scrollLeft += (r.left - c.left) - c.width/3;
      }
    }
    // ¿por qué salida va a salir la condición que va a ejecutarse en el paso k?
    function salida(tr, k){
      const s = tr[k], n = tr[k+1]; if (!s || !n) return null;
      const H = heads.find(H => s.l>=H.a && s.l<=H.z); if (!H) return null;
      return {kind:H.kind, r: H.si.has(n.l) ? 'si' : 'no'};
    }
    return {html, conecta, pinta, salida};
  }
  return {crea, CSS};
})();
