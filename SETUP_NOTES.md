# Site Setup Notes - Tuesday's Researcher Profile

## ✅ Completed Updates

### 1. **Site Configuration** (`_config.yml`)
- ✅ Updated site title to "Tuesday (Claudia Ramirez)"
- ✅ Set proper name fields (first_name, middle_name, last_name)
- ✅ Updated description with ARTIFEX Labs bio
- ✅ Changed URL to `https://tuesdaythe13th.github.io`
- ✅ Set baseurl to empty (root deployment)
- ✅ Updated favicon icon to 🔬
- ✅ Updated blog name to "ARTIFEX Labs Research"
- ✅ Updated blog description
- ✅ Updated Jekyll Scholar settings with your name

### 2. **About Page** (`_pages/about.md`)
- ✅ Updated subtitle with your role and affiliation
- ✅ Replaced placeholder bio with your actual biography
- ✅ Updated contact info to tuesday@artifex.fun
- ✅ Removed placeholder address fields

### 3. **Social Media Links** (`_data/socials.yml`)
- ✅ Email: tuesday@artifex.fun
- ✅ GitHub: tuesdaythe13th
- ✅ LinkedIn: 222tuesday
- ✅ Google Scholar: z71m_nIAAAAJ
- ✅ X/Twitter: artifexlabs
- ✅ Work URL: https://artifex.fun

## 🚀 Next Steps

### To Deploy This Site:

#### Option 1: Deploy to `Tuesdaythe13th.github.io` (Main GitHub Pages Site)
This would replace your current Hugo Blox site with this Jekyll al-folio theme.

1. **Rename this repository** on GitHub:
   - Go to https://github.com/Tuesdaythe13th/semiotic_collapse/settings
   - Change repository name to: `Tuesdaythe13th.github.io`
   
2. **Push your changes**:
   ```bash
   cd /Users/tuesday/Desktop/semiotic_collapse
   git add .
   git commit -m "Personalize site with ARTIFEX Labs profile"
   git push origin main
   ```

3. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Source: Deploy from branch `main`
   - Folder: `/ (root)`
   - Save

#### Option 2: Keep Both Sites (Recommended)
Keep your Hugo Blox site at `Tuesdaythe13th.github.io` and deploy this as a subsite:

1. **Deploy as subdirectory** (e.g., `tuesdaythe13th.github.io/research`):
   - Update `_config.yml` line 22: `baseurl: /research`
   - Push changes to the `semiotic_collapse` repo
   - Enable GitHub Pages in that repo's settings

2. **Or use a custom domain** for this site

### Before Deploying:

1. **Install Jekyll locally** to preview:
   ```bash
   # Install Ruby and Bundler first
   bundle install
   bundle exec jekyll serve
   ```
   Then visit http://localhost:4000

2. **Add a profile picture**:
   - Add your photo as `assets/img/prof_pic.jpg`

3. **Update publications**:
   - Edit `_bibliography/papers.bib` with your publications

4. **Customize projects**:
   - Add your projects in `_projects/` folder

5. **Add news items**:
   - Add announcements in `_news/` folder

## 📝 Current Repository Status

- **Repository**: https://github.com/Tuesdaythe13th/semiotic_collapse
- **Local Path**: `/Users/tuesday/Desktop/semiotic_collapse`
- **Modified Files**: 
  - `_config.yml`
  - `_data/socials.yml`
  - `_pages/about.md`
- **Status**: Changes not yet committed

## 🎨 Theme Information

This site uses the **al-folio** Jekyll theme, which is:
- Clean, academic-focused design
- Built-in support for publications (BibTeX)
- Blog functionality
- Project showcases
- Dark/Light mode
- Responsive and mobile-friendly

## 📚 Documentation

- [al-folio Documentation](https://github.com/alshedivat/al-folio)
- [Customization Guide](CUSTOMIZE.md)
- [Installation Guide](INSTALL.md)
- [FAQ](FAQ.md)
