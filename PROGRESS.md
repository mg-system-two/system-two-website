# System Two Website Redesign - Progress Tracker

## Project Goal
Implement dark green color scheme on the system-two.org website.

**FOCUS:** Visual design only - Colors, Fonts/Typography, Layouts
**NOT TODAY:** Written content (comes later)

## Project Date
Started: March 5, 2026

---

## Phase 1: Setup ✅ COMPLETE

- [x] Install Git/Xcode Command Line Tools
- [x] Clone repository from GitHub
- [x] Review current website structure
- [x] Analyze design aesthetic

---

## Phase 2: Visual Design Development ✅ COMPLETE

### Core Focus:
- [x] **Colors** - Dark green palette (#1a3a30, #2C5F4F, #5a8a7a, #7daa98)
- [x] **Fonts/Typography** - Arial, size hierarchy, letter spacing
- [x] **Layouts** - Grid systems, card layouts, spacing structure

### Files Modified:
- [x] css/styles.css - Complete visual styling system with green theme

### May Work On Later:
- [ ] Spacing/Whitespace refinements
- [ ] Borders & Lines details
- [ ] Shadows & Depth
- [ ] Animations/Transitions
- [ ] Icons
- [ ] Button styles
- [ ] Border radius adjustments

---

## Phase 3: Git Operations ✅ COMPLETE

### Steps:
- [x] Set up SSH keys for GitHub
- [x] Navigate to repository: `cd ~/Desktop/system-two-website`
- [x] Check status: `git status`
- [x] Stage changes: `git add css/styles.css`
- [x] Commit changes: `git commit -m "Add green color scheme"`
- [x] Push to GitHub: `git push origin main`

---

## Phase 4: Server Deployment ✅ COMPLETE

### Steps:
- [x] Set up SSH deploy key on Digital Ocean droplet
- [x] Configure git remote to use SSH
- [x] Pull changes to server: `git pull origin main`
- [x] Set up SSL certificate with Let's Encrypt
- [x] Configure nginx for www and non-www domains

---

## Phase 5: Verification ✅ COMPLETE

### Steps:
- [x] Visit system-two.org - GREEN! 🟢
- [x] Visit www.system-two.org - GREEN! 🟢
- [x] Verify HTTPS works - SECURE! 🔒
- [x] Test all pages
- [x] Verify navigation links work

---

## Phase 6: Refinements ⏳ PENDING

### Potential improvements:
- [ ] Add favicon
- [ ] Add logo image if available
- [ ] Create additional programme detail pages
- [ ] Add images if needed
- [ ] SEO optimization
- [ ] Analytics setup
- [ ] Set up automated deployment (GitHub Actions)

---

## Notes

### Repository Location
- Local: `~/Desktop/system-two-website`
- GitHub: `https://github.com/mg-system-two/system-two-website`
- Server: `/var/www/html` on Digital Ocean droplet

### Design Colors
- Key colors: Dark green (#1a3a30), Medium green (#2C5F4F), Accent green (#7daa98)

### Deployment Process
To update the live site:
1. Make changes locally
2. Commit and push to GitHub: `git push origin main`
3. SSH to server (or use Digital Ocean console)
4. Run: `su - deploy && cd /var/www/html && git pull origin main`

### Current Status
**Phase 5:** COMPLETE - Site is live with green theme and HTTPS! 🎉

---

## Questions / Issues
_Track any problems or questions here_

- Mac SSH to Digital Ocean still not working (using console for now)

---

**Last Updated:** March 6, 2026
**Status:** Green theme successfully deployed! 🟢🔒
