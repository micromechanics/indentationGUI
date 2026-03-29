document.addEventListener("DOMContentLoaded", () => {
  const codeBlocks = document.querySelectorAll("div.highlight");

  const copyText = async (text) => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }

    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "absolute";
    textarea.style.left = "-9999px";
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
  };

  codeBlocks.forEach((block) => {
    if (block.dataset.copyButtonAdded === "true") {
      return;
    }

    const pre = block.querySelector("pre");
    if (!pre) {
      return;
    }

    const button = document.createElement("button");
    button.type = "button";
    button.className = "copy-code-button";
    button.textContent = "Copy";
    button.setAttribute("aria-label", "Copy code");

    button.addEventListener("click", async () => {
      const originalLabel = "Copy";
      const copiedLabel = "Copied";
      const failedLabel = "Failed";
      const codeText = pre.textContent.replace(/\s+$/, "");

      try {
        await copyText(codeText);
        button.textContent = copiedLabel;
        button.classList.add("is-copied");
      } catch (error) {
        console.error("Failed to copy code block", error);
        button.textContent = failedLabel;
      }

      window.setTimeout(() => {
        button.textContent = originalLabel;
        button.classList.remove("is-copied");
      }, 1400);
    });

    block.appendChild(button);
    block.dataset.copyButtonAdded = "true";
  });
});
