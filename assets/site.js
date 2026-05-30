/* ai-beginner-guide-2026 — shared site script (page-independent).
   Powers: theme toggle, content-freshness display, ⌘K search command palette.
   Loaded on every page via <script src=".../assets/site.js" defer>.
   Site root is derived from this script's own URL, so the same file works
   at the site root (index) and in /guides/ without per-page path injection. */
(function () {
  var self = document.querySelector('script[src$="site.js"]');
  var SITEROOT = self ? new URL('..', self.src).href : new URL('.', location.href).href;
  var BASEPATH = new URL(SITEROOT).pathname;

  /* ---- theme toggle ---- */
  (function () {
    var b = document.getElementById("themeToggle");
    if (!b) return;
    b.addEventListener("click", function () {
      var d = document.documentElement;
      var nx = d.getAttribute("data-theme") === "dark" ? "light" : "dark";
      d.setAttribute("data-theme", nx);
      try { localStorage.setItem("theme", nx); } catch (e) {}
    });
  })();

  /* ---- content freshness ---- */
  (function () {
    var lu = document.querySelector('meta[name=last-updated]'), lv = document.querySelector('meta[name=last-verified]');
    if (lu) document.querySelectorAll('.lu').forEach(function (e) { e.textContent = lu.content; });
    if (lv) {
      if (new Date(lv.content) > new Date(lu ? lu.content : 0)) {
        document.querySelectorAll('.lv').forEach(function (e) { e.textContent = lv.content; });
        document.querySelectorAll('.lv-wrap').forEach(function (e) { e.hidden = false; });
      }
      var d = (Date.now() - new Date(lv.content).getTime()) / 86400000;
      if (d > 180) {
        var w = document.querySelector('.stale-warn');
        if (w) { w.classList.add('show'); w.hidden = false; w.querySelector('span').textContent = '本篇最後驗證於 ' + lv.content + '，AI 工具更新快，部分資訊可能已變動。'; }
      }
    }
  })();

  /* ---- ⌘K search command palette (Pagefind JS API) ---- */
  (function () {
    var PFURL = SITEROOT + 'pagefind/pagefind.js';
    var CAT = { '基礎觀念': 'cb', '平台工具': 'ct', '進階·Agent': 'ca', '流程·應用': 'cf' };
    var modal = document.getElementById('searchModal'), input = document.getElementById('searchInput'), box = document.getElementById('searchResults'), trig = document.getElementById('searchTrigger');
    if (!modal || !input || !box) return;
    var pf = null, items = [], act = -1, seq = 0, tmr;
    function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]; }); }
    function hint() { box.innerHTML = '<div class="sm-msg">輸入關鍵字，搜尋 11 篇指南…</div>'; items = []; act = -1; }
    function open() { modal.hidden = false; document.documentElement.style.overflow = 'hidden'; if (!input.value) hint(); setTimeout(function () { input.focus(); }, 20); }
    function close() { modal.hidden = true; document.documentElement.style.overflow = ''; act = -1; }
    function setAct(i) { if (!items.length) return; act = (i + items.length) % items.length; items.forEach(function (el, k) { el.classList.toggle('active', k === act); if (k === act) el.scrollIntoView({ block: 'nearest' }); }); }
    async function ensure() { if (!pf) { pf = await import(PFURL); } return pf; }
    async function run(q) {
      var my = ++seq; if (!q) { hint(); return; }
      box.innerHTML = '<div class="sm-msg">正在搜尋「' + esc(q) + '」…</div>';
      try {
        var p = await ensure(); var s = await p.search(q); if (my !== seq) return;
        var all = s.results; var top = all.length ? all[0].score : 0; var floor = Math.max(1, 0.2 * top);
        var keep = all.filter(function (r) { return r.score >= floor; }).slice(0, 8);
        var d = await Promise.all(keep.map(function (r) { return r.data(); })); if (my !== seq) return;
        draw(q, d);
      } catch (e) { box.innerHTML = '<div class="sm-msg">搜尋失敗</div>'; }
    }
    function draw(q, d) {
      if (!d.length) { box.innerHTML = '<div class="sm-msg">找不到「' + esc(q) + '」的結果</div>'; items = []; act = -1; return; }
      var h = '';
      d.forEach(function (x, i) {
        var tag = (x.meta && x.meta.tag) || ''; var cat = tag.split(' · ')[0] || ''; var cls = CAT[cat] || 'cg';
        var u = String(x.url);
        var href = u.indexOf(BASEPATH) === 0 ? location.origin + u : location.origin + BASEPATH.replace(/\/+$/, '') + (u.charAt(0) === '/' ? u : '/' + u);
        var ti = (x.meta && x.meta.title) || x.url;
        h += '<a class="sm-item' + (i === 0 ? ' active' : '') + '" role="option" href="' + href + '"><svg class="sm-i" viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M5 8V5a2 2 0 0 1 2-2h7l5 5v11a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-3"/></svg><span class="sm-title">' + esc(ti) + '</span>' + (cat ? '<span class="chip ' + cls + '">' + esc(cat) + '</span>' : '') + '</a>';
      });
      box.innerHTML = h; items = Array.prototype.slice.call(box.querySelectorAll('.sm-item')); act = items.length ? 0 : -1;
    }
    input.addEventListener('input', function () { clearTimeout(tmr); var q = input.value.trim(); tmr = setTimeout(function () { run(q); }, 170); });
    if (trig) trig.addEventListener('click', open);
    modal.addEventListener('click', function (e) { if (e.target === modal || (e.target.classList && e.target.classList.contains('sm-backdrop')) || e.target.id === 'searchClose') close(); });
    document.addEventListener('keydown', function (e) {
      var k = e.key;
      if ((e.metaKey || e.ctrlKey) && (k === 'k' || k === 'K')) { e.preventDefault(); modal.hidden ? open() : close(); return; }
      if (modal.hidden) { if (k === '/') { var tn = (e.target && e.target.tagName) || ''; if (tn !== 'INPUT' && tn !== 'TEXTAREA' && !(e.target && e.target.isContentEditable)) { e.preventDefault(); open(); } } return; }
      if (k === 'Escape') { close(); }
      else if (k === 'ArrowDown') { e.preventDefault(); setAct(act + 1); }
      else if (k === 'ArrowUp') { e.preventDefault(); setAct(act - 1); }
      else if (k === 'Enter') { if (act >= 0 && items[act]) { window.location.href = items[act].getAttribute('href'); } }
    });
  })();
})();
