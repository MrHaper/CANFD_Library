// mermaid 初始化:页面加载后启动图表渲染
document.addEventListener("DOMContentLoaded", function () {
  if (typeof mermaid !== "undefined") {
    mermaid.initialize({ startOnLoad: true, theme: "default" });
  }
});
