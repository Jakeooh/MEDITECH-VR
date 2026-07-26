# How to Deploy Meditech VR for Free

Your specific VR application is a "Static Web App" (HTML + JavaScript). This means it is very easy to host for free!

**Prerequisite:**
You need the files I created. They are located in:
`C:\Users\anfyj\.gemini\antigravity\scratch\MedicardWebVR`

---

## Option 1: Netlify Drop (Easiest - Recommended)
**Best for: Non-coders, instant drag-and-drop.**

1.  Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2.  Open your file explorer to `C:\Users\anfyj\.gemini\antigravity\scratch`.
3.  **Drag and Drop** the entire `MedicardWebVR` folder onto the Netlify page box that says "Drag and drop your site folder here".
4.  Netlify will upload it and give you a random URL (e.g., `silly-salamander-123456.netlify.app`).
5.  **Done!** Open that link on your phone.
    *   *Note: Netlify provides free HTTPS, which is required for the Camera to work.*

---

## Option 2: GitHub Pages
**Best for: If you want to keep the code safe and use a cleaner URL.**

1.  Create a new Repository on GitHub (e.g., `meditech-vr`).
2.  Upload the files (`index.html`, `js/`, `assets/`) to that repository.
3.  Go to **Settings** > **Pages**.
4.  Under "Branch", select `main` (or `master`) and hit **Save**.
5.  GitHub will give you a link like `https://yourname.github.io/meditech-vr`.

---

## Important Check
Before sharing, ensure you are accessing the site via **HTTPS** (https://...) and not HTTP. The camera will NOT open on a phone if the site is not secure. Both Netlify and GitHub Pages force HTTPS automatically.
