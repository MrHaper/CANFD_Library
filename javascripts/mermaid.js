/* CAN FD 知识库 Mermaid 初始化:统一中文字体、配色,并随站点深浅色主题重绘 */
(function () {
  "use strict";

  if (typeof mermaid === "undefined") {
    return;
  }

  var FONT =
    '"Roboto","Helvetica Neue","PingFang SC","Microsoft YaHei","Noto Sans SC",sans-serif';

  function isDark() {
    return (
      document.documentElement.getAttribute("data-md-color-scheme") === "slate"
    );
  }

  function diagramConfig() {
    var dark = isDark();
    return {
      startOnLoad: false,
      securityLevel: "loose",
      maxTextSize: 90000,
      fontFamily: FONT,
      theme: "base",
      themeVariables: {
        fontFamily: FONT,
        fontSize: "16px",
        primaryColor: dark ? "#1f2a44" : "#eaf1fb",
        primaryBorderColor: dark ? "#7aa2f7" : "#0f4c81",
        primaryTextColor: dark ? "#e6edf3" : "#0f172a",
        lineColor: dark ? "#8b949e" : "#52677a",
        secondaryColor: dark ? "#4a3a1a" : "#fff3dd",
        secondaryBorderColor: dark ? "#e2a13f" : "#d97706",
        secondaryTextColor: dark ? "#f3e2c4" : "#5b3a12",
        tertiaryColor: dark ? "#16382d" : "#e7f6ef",
        tertiaryBorderColor: dark ? "#56d4a0" : "#0e9f6e",
        tertiaryTextColor: dark ? "#d8f3e7" : "#0b4b37",
        clusterBkg: dark ? "#161b22" : "#f8fafc",
        clusterBorder: dark ? "#30363d" : "#cbd5e1",
        edgeLabelBackground: dark ? "#0d1117" : "#ffffff",
        actorBkg: dark ? "#1f2a44" : "#eaf1fb",
        actorBorder: dark ? "#7aa2f7" : "#0f4c81",
        actorTextColor: dark ? "#e6edf3" : "#0f172a",
        actorLineColor: dark ? "#8b949e" : "#94a3b8",
        signalColor: dark ? "#8b949e" : "#52677a",
        signalTextColor: dark ? "#e6edf3" : "#0f172a",
        labelBoxBkgColor: dark ? "#1f2a44" : "#eaf1fb",
        labelBoxBorderColor: dark ? "#7aa2f7" : "#0f4c81",
        labelTextColor: dark ? "#e6edf3" : "#0f172a",
        loopTextColor: dark ? "#e6edf3" : "#0f172a",
        noteBkgColor: dark ? "#4a3a1a" : "#fff3dd",
        noteBorderColor: dark ? "#e2a13f" : "#d97706",
        noteTextColor: dark ? "#f3e2c4" : "#5b3a12",
        activationBkgColor: dark ? "#3d4657" : "#dbe6f5",
        activationBorderColor: dark ? "#7aa2f7" : "#0f4c81",
        sequenceNumberColor: dark ? "#0d1117" : "#ffffff"
      },
      flowchart: {
        curve: "basis",
        padding: 16,
        htmlLabels: true,
        wrappingWidth: 90
      },
      sequence: {
        mirrorActors: false,
        actorMargin: 55,
        boxMargin: 10,
        messageMargin: 42,
        showSequenceNumbers: true
      },
      class: { useMaxWidth: true },
      state: { useMaxWidth: true },
      er: { useMaxWidth: true },
      journey: { useMaxWidth: true },
      gantt: { useMaxWidth: true },
      pie: { useMaxWidth: true },
      quadrantChart: { useMaxWidth: true },
      requirement: { useMaxWidth: true },
      c4: { useMaxWidth: true },
      mindmap: { useMaxWidth: true, padding: 14 }
    };
  }

  function captureSource(el) {
    if (!el.getAttribute("data-src")) {
      el.setAttribute("data-src", el.textContent || "");
    }
  }

  function renderAll() {
    var nodes = document.querySelectorAll(".mermaid");
    nodes.forEach(captureSource);
    mermaid.run({ querySelector: ".mermaid" }).catch(function (err) {
      console.error("Mermaid render failed:", err);
    });
  }

  function rerender() {
    var nodes = document.querySelectorAll(".mermaid");
    nodes.forEach(function (el) {
      var src = el.getAttribute("data-src");
      if (src === null) {
        return;
      }
      el.removeAttribute("data-processed");
      el.textContent = "";
      el.innerHTML = "";
      el.textContent = src;
    });
    renderAll();
  }

  function setup() {
    mermaid.initialize(diagramConfig());
    renderAll();

    // 深浅色主题切换时,用新配色重绘全部图表
    var observer = new MutationObserver(function () {
      mermaid.initialize(diagramConfig());
      rerender();
    });
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-md-color-scheme"]
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setup);
  } else {
    setup();
  }
})();
