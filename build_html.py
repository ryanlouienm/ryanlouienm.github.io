import base64

with open('/Users/ryanlouienolasco/.gemini/antigravity/scratch/ryan-links/profile.jpg', 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

with open('/Users/ryanlouienolasco/.gemini/antigravity/scratch/ryan-links/rednote_clean.png', 'rb') as f:
    b64_xhs = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>RYAN Links</title>
  <meta name="description" content="K-POP DANCE COVERS · OʻAHU, HAWAIʻI — Dance reels, practice cuts & polished covers by Ryan Louie Nolasco (@ryanlouienm)">
  <link rel="icon" type="image/jpeg" href="data:image/jpeg;base64,{b64_img}">
  <link rel="apple-touch-icon" href="data:image/jpeg;base64,{b64_img}">
  <meta name="theme-color" content="#DCEEFB">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  
  <style>
    :root {{
      --bg-color: #dceefb;
      --navy-dark: #0f2b5c;
      --royal-blue: #1b45cb;
      --royal-accent: #2550d4;
      --text-muted: #507294;
      --text-bio: #4a6888;
      --btn-arrow-bg: #e2effc;
      --card-white: #ffffff;
      --card-shadow: 0 4px 18px rgba(15, 43, 92, 0.05);
      --card-hover-shadow: 0 8px 24px rgba(27, 69, 203, 0.12);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      min-height: 100vh;
      background-color: var(--bg-color);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      color: var(--navy-dark);
      position: relative;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    /* Background Organic Waves matching Muse */
    .bg-waves {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }}

    .bg-svg {{
      width: 100%;
      height: 100%;
      display: block;
    }}

    /* Main Container */
    .container {{
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 440px;
      margin: 0 auto;
      padding: 32px 18px 48px 18px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    /* Hero Section directly on background */
    .hero {{
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin-bottom: 24px;
    }}

    /* Avatar & Sparkles */
    .avatar-wrap {{
      position: relative;
      width: 120px;
      height: 120px;
      margin: 0 auto 16px auto;
    }}

    .avatar-img {{
      width: 120px;
      height: 120px;
      border-radius: 50%;
      object-fit: cover;
      display: block;
      border: 3.5px solid #ffffff;
      box-shadow: 0 0 0 2.5px var(--royal-accent), 0 8px 22px rgba(27, 69, 203, 0.18);
    }}

    .sparkle {{
      position: absolute;
      pointer-events: none;
      animation: floatSparkle 4s ease-in-out infinite alternate;
    }}

    .sparkle-left {{
      top: 14px;
      left: -14px;
      width: 17px;
      height: 17px;
    }}

    .sparkle-right {{
      top: 64px;
      right: -16px;
      width: 15px;
      height: 15px;
      animation-delay: 2s;
    }}

    @keyframes floatSparkle {{
      0% {{ transform: translateY(0) scale(1); }}
      50% {{ transform: translateY(-3px) scale(1.08); }}
      100% {{ transform: translateY(2px) scale(0.95); }}
    }}

    /* Hero Typography */
    .brand-title {{
      font-size: 38px;
      font-weight: 900;
      color: var(--navy-dark);
      letter-spacing: 0.5px;
      line-height: 1.1;
      margin-bottom: 4px;
    }}

    .name-sub {{
      font-size: 19px;
      font-weight: 700;
      color: var(--royal-accent);
      margin-bottom: 12px;
    }}

    .tagline {{
      font-size: 12.5px;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 1.6px;
      text-transform: uppercase;
      margin-bottom: 14px;
    }}

    .bio {{
      font-size: 14.5px;
      font-weight: 500;
      color: var(--text-bio);
      line-height: 1.55;
      max-width: 390px;
      margin-bottom: 18px;
    }}

    .bio strong {{
      color: var(--navy-dark);
      font-weight: 800;
    }}

    /* Chapter 2 Pill */
    .chapter-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--royal-blue);
      color: #ffffff;
      padding: 8px 18px;
      border-radius: 999px;
      font-size: 12.5px;
      font-weight: 800;
      letter-spacing: 0.8px;
      box-shadow: 0 4px 14px rgba(27, 69, 203, 0.28);
      margin-bottom: 14px;
    }}

    .pill-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #73b8ff;
      display: inline-block;
    }}

    /* Chapter Story Text */
    .chapter-story {{
      font-size: 14px;
      font-weight: 500;
      color: var(--text-bio);
      line-height: 1.55;
      max-width: 400px;
      margin: 0 auto 20px auto;
    }}

    .chapter-story strong {{
      color: var(--navy-dark);
      font-weight: 700;
    }}

    /* Handle: ONLY @ryanlouienm, underlined in blue, no bubble */
    .handle-wrap {{
      text-align: center;
      margin: 4px 0 6px 0;
    }}

    .handle-link {{
      font-size: 22px;
      font-weight: 800;
      color: var(--navy-dark);
      text-decoration: underline;
      text-decoration-color: var(--royal-accent);
      text-decoration-thickness: 3px;
      text-underline-offset: 6px;
      letter-spacing: 0.3px;
      display: inline-block;
    }}

    /* Links Stack */
    .links-stack {{
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 20px;
    }}

    .link-card {{
      background: var(--card-white);
      border-radius: 20px;
      padding: 14px 18px;
      box-shadow: var(--card-shadow);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      text-decoration: none;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }}

    .link-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--card-hover-shadow);
    }}

    .link-card:active {{
      transform: scale(0.985);
    }}

    .card-left {{
      display: flex;
      align-items: center;
      gap: 14px;
      min-width: 0;
      flex: 1;
    }}

    .card-icon-wrap {{
      width: 46px;
      height: 46px;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* Icon Variations */
    .icon-ig {{
      border-radius: 13px;
      background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
      box-shadow: 0 3px 10px rgba(214, 36, 159, 0.25);
    }}

    .icon-fb {{
      border-radius: 50%;
      background: #e2effc;
    }}

    .icon-tiktok {{
      border-radius: 50%;
      background: #000000;
    }}

    .icon-yt {{
      border-radius: 50%;
      background: #feebeb;
    }}

    .icon-xhs {{
      border-radius: 13px;
      overflow: hidden;
      box-shadow: 0 3px 10px rgba(255, 36, 66, 0.25);
    }}

    .icon-xhs-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}

    .card-text {{
      display: flex;
      flex-direction: column;
      gap: 3px;
      min-width: 0;
      text-align: left;
    }}

    .card-title {{
      font-size: 16.5px;
      font-weight: 800;
      color: var(--navy-dark);
      line-height: 1.25;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .card-sub {{
      font-size: 13px;
      font-weight: 500;
      color: var(--text-muted);
      line-height: 1.3;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* Arrow Button on the right */
    .card-action {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--btn-arrow-bg);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: background-color 0.15s ease, transform 0.15s ease;
    }}

    .link-card:hover .card-action {{
      background: #d4e7fb;
      transform: translateX(2px) translateY(-2px);
    }}

    /* About Ryan Card */
    .about-card {{
      width: 100%;
      background: var(--card-white);
      border-radius: 22px;
      padding: 24px 22px;
      box-shadow: var(--card-shadow);
      text-align: center;
      margin-bottom: 28px;
    }}

    .about-header {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      font-size: 13.5px;
      font-weight: 800;
      letter-spacing: 1.6px;
      color: var(--royal-blue);
      margin-bottom: 12px;
      text-transform: uppercase;
    }}

    .about-star {{
      font-size: 14px;
      color: var(--royal-accent);
    }}

    .about-desc {{
      font-size: 14.5px;
      font-weight: 500;
      color: var(--text-bio);
      line-height: 1.6;
      text-align: center;
    }}

    .about-desc strong {{
      color: var(--navy-dark);
      font-weight: 800;
    }}

    /* Footer */
    .footer-section {{
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }}

    .footer-title {{
      font-size: 17.5px;
      font-weight: 800;
      color: var(--navy-dark);
    }}

    .footer-sub {{
      font-size: 13.5px;
      font-weight: 500;
      color: var(--text-muted);
    }}

    @media (max-width: 380px) {{
      .container {{
        padding: 24px 14px 40px 14px;
      }}
      .brand-title {{
        font-size: 34px;
      }}
      .link-card {{
        padding: 12px 14px;
      }}
      .card-title {{
        font-size: 15.5px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Background organic wavy canvas -->
  <div class="bg-waves" aria-hidden="true">
    <svg class="bg-svg" viewBox="0 0 500 1200" preserveAspectRatio="xMidYMin slice">
      <!-- Top wave behind avatar & right of hero -->
      <path d="M 110 -20 C 240 30, 360 80, 420 180 C 470 270, 520 380, 520 480 C 420 500, 320 460, 260 410 C 200 350, 220 250, 270 210 C 310 170, 290 90, 190 60 C 150 48, 120 15, 110 -20 L 520 -20 L 520 480 Z" fill="#ffffff"/>
      <!-- Mid wave behind Facebook & TikTok -->
      <path d="M -20 540 C 90 530, 210 580, 230 680 C 250 780, 150 860, -20 880 Z" fill="#ffffff"/>
      <!-- Bottom wave behind About card and footer -->
      <path d="M 520 860 C 410 870, 300 930, 280 1030 C 260 1130, 360 1210, 520 1220 Z" fill="#ffffff"/>
    </svg>
  </div>

  <main class="container">
    
    <!-- Hero Section (direct on background) -->
    <header class="hero">
      
      <div class="avatar-wrap">
        <!-- Sparkle Top-Left (Light Sky Blue) -->
        <svg class="sparkle sparkle-left" viewBox="0 0 24 24" fill="#62b5ec" aria-hidden="true">
          <path d="M12 0C12 6.627 6.627 12 0 12C6.627 12 12 17.373 12 24C12 17.373 17.373 12 24 12C17.373 12 12 6.627 12 0Z"/>
        </svg>
        
        <img src="data:image/jpeg;base64,{b64_img}" alt="Ryan Louie Nolasco" class="avatar-img">
        
        <!-- Sparkle Mid-Right (Royal Dark Blue) -->
        <svg class="sparkle sparkle-right" viewBox="0 0 24 24" fill="#1b45cb" aria-hidden="true">
          <path d="M12 0C12 6.627 6.627 12 0 12C6.627 12 12 17.373 12 24C12 17.373 17.373 12 24 12C17.373 12 12 6.627 12 0Z"/>
        </svg>
      </div>

      <h1 class="brand-title">RYAN</h1>
      <div class="name-sub">Ryan Louie Nolasco</div>
      <div class="tagline">K-POP DANCE COVERS &nbsp;·&nbsp; OʻAHU, HAWAIʻI</div>

      <p class="bio">Dance reels, practice cuts &amp; polished covers — <strong>posted everywhere, same reel.</strong> New drops all through Chapter 2.</p>

      <div class="chapter-pill">
        <span class="pill-dot"></span>
        <span>CHAPTER 2: PAINT THE WORLD</span>
      </div>

      <p class="chapter-story"><strong>Chapter 1: Awakening The Ace</strong> came first. Now <strong>Chapter 2: Paint The World</strong> is about being fully yourself, no matter what. Hate is inevitable and will come regardless — but to put yourself out there, you must paint the world!</p>

      <div class="handle-wrap">
        <span class="handle-link">@ryanlouienm</span>
      </div>

    </header>

    <!-- Links Stack -->
    <nav class="links-stack" aria-label="Official Links">

      <!-- 1. Instagram -->
      <a href="https://www.instagram.com/ryanlouienm?xtok=Y25yaHUyZ3BseW43&amp;utm_source=qr" 
         target="_blank" 
         rel="noopener noreferrer" 
         class="link-card" 
         aria-label="Instagram: Reels, stories &amp; updates">
        <div class="card-left">
          <div class="card-icon-wrap icon-ig">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
              <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            </svg>
          </div>
          <div class="card-text">
            <span class="card-title">Instagram</span>
            <span class="card-sub">Reels, stories &amp; updates</span>
          </div>
        </div>
        <div class="card-action" aria-hidden="true">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#1b45cb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </div>
      </a>

      <!-- 2. Facebook -->
      <a href="https://www.facebook.com/share/1JpFRVHH4j/?mibextid=wwXIfr" 
         target="_blank" 
         rel="noopener noreferrer" 
         class="link-card" 
         aria-label="Facebook: Reels, updates &amp; community posts">
        <div class="card-left">
          <div class="card-icon-wrap icon-fb">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="#1877f2">
              <path d="M14 13.5h2.5l1-4H14v-2c0-1.03.3-1.75 1.75-1.75H17.5V2.2c-.37-.05-1.5-.15-2.85-.15-2.82 0-4.65 1.72-4.65 4.77v2.68H6.5v4H10v10.5h4V13.5z"/>
            </svg>
          </div>
          <div class="card-text">
            <span class="card-title">Facebook</span>
            <span class="card-sub">Reels, updates &amp; community posts</span>
          </div>
        </div>
        <div class="card-action" aria-hidden="true">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#1b45cb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </div>
      </a>

      <!-- 3. TikTok -->
      <a href="https://www.tiktok.com/@ryanlouienm?_r=1&amp;_t=ZT-9AxGZhjOUbm" 
         target="_blank" 
         rel="noopener noreferrer" 
         class="link-card" 
         aria-label="TikTok: Daily dance TikToks">
        <div class="card-left">
          <div class="card-icon-wrap icon-tiktok">
            <svg width="21" height="21" viewBox="0 0 24 24" fill="#ffffff">
              <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64c.298 0 .586.046.86.13V9.42a6.34 6.34 0 0 0-.86-.06 6.34 6.34 0 1 0 6.34 6.34V8.58a8.28 8.28 0 0 0 4.77 1.52v-3.41z"/>
            </svg>
          </div>
          <div class="card-text">
            <span class="card-title">TikTok</span>
            <span class="card-sub">Daily dance TikToks</span>
          </div>
        </div>
        <div class="card-action" aria-hidden="true">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#1b45cb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </div>
      </a>

      <!-- 4. YouTube -->
      <a href="https://youtube.com/@ryanlouienm?si=k9ac4z_xhN1ph43_" 
         target="_blank" 
         rel="noopener noreferrer" 
         class="link-card" 
         aria-label="YouTube: Shorts &amp; covers">
        <div class="card-left">
          <div class="card-icon-wrap icon-yt">
            <svg width="25" height="18" viewBox="0 0 24 17" fill="none">
              <path d="M23.498 2.628a2.998 2.998 0 0 0-2.11-2.12C19.52 0 12 0 12 0S4.48 0 2.612.508a2.998 2.998 0 0 0-2.11 2.12C0 4.506 0 8.5 0 8.5s0 3.994.502 5.872a2.998 2.998 0 0 0 2.11 2.12C4.48 17 12 17 12 17s7.52 0 9.388-.508a2.998 2.998 0 0 0 2.11-2.12C24 12.494 24 8.5 24 8.5s0-3.994-.502-5.872z" fill="#FF0000"/>
              <polygon points="9.6 12.1 15.84 8.5 9.6 4.9" fill="#FFFFFF"/>
            </svg>
          </div>
          <div class="card-text">
            <span class="card-title">YouTube</span>
            <span class="card-sub">Shorts &amp; covers</span>
          </div>
        </div>
        <div class="card-action" aria-hidden="true">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#1b45cb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </div>
      </a>

      <!-- 5. rednote 小红书 -->
      <a href="https://xhslink.cn/m/A94wY75Vcx1" 
         target="_blank" 
         rel="noopener noreferrer" 
         class="link-card" 
         aria-label="rednote 小红书: Notes &amp; dance covers">
        <div class="card-left">
          <div class="card-icon-wrap icon-xhs">
            <img src="data:image/png;base64,{b64_xhs}" alt="rednote" class="icon-xhs-img">
          </div>
          <div class="card-text">
            <span class="card-title">rednote 小红书</span>
            <span class="card-sub">Notes &amp; dance covers</span>
          </div>
        </div>
        <div class="card-action" aria-hidden="true">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#1b45cb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </div>
      </a>

    </nav>

    <!-- About Ryan Card -->
    <section class="about-card" aria-label="About Ryan">
      <div class="about-header">
        <span class="about-star">✦</span>
        <span>ABOUT RYAN</span>
        <span class="about-star">✦</span>
      </div>
      <p class="about-desc">
        Ryan is a <strong>boy dancer</strong> from Oʻahu who specializes in <strong>K-pop dance and performance</strong> — sharp, high-energy covers posted as simple reels, one track at a time.
      </p>
    </section>

    <!-- Footer -->
    <footer class="footer-section">
      <h2 class="footer-title">Check out Ryan's content!</h2>
      <p class="footer-sub">Tap a link above to watch on your favorite platform.</p>
    </footer>

  </main>

</body>
</html>
'''

with open('/Users/ryanlouienolasco/.gemini/antigravity/scratch/ryan-links/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully!")
