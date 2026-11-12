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
  <meta name="theme-color" content="#AEDFF2">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  
  <style>
    :root {{
      --light-blue: #AEDFF2;
      --pastel-pink: #F7C8D8;
      --neutral-blue: #7AA0C4;
      --royal-blue: #243FD6;
      --royal-dark: #162E7B;
      --white: #FFFFFF;
      --text-main: #0D1B3E;
      --text-muted: #5B6F86;
      --card-bg: rgba(255, 255, 255, 0.86);
      --card-border: rgba(255, 255, 255, 0.95);
      --card-shadow: 0 8px 24px rgba(22, 46, 123, 0.07);
      --card-hover-shadow: 0 14px 32px rgba(36, 63, 214, 0.14);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      min-height: 100vh;
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: #F0F6FB;
      background-image: 
        radial-gradient(circle at 12% 12%, rgba(174, 223, 242, 0.85) 0%, transparent 45%),
        radial-gradient(circle at 88% 18%, rgba(247, 200, 216, 0.70) 0%, transparent 42%),
        radial-gradient(circle at 50% 50%, rgba(122, 160, 196, 0.35) 0%, transparent 55%),
        radial-gradient(circle at 20% 85%, rgba(174, 223, 242, 0.60) 0%, transparent 45%),
        radial-gradient(circle at 82% 88%, rgba(36, 63, 214, 0.18) 0%, transparent 45%);
      background-attachment: fixed;
      color: var(--text-main);
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 40px 18px 60px;
      line-height: 1.5;
    }}

    .container {{
      width: 100%;
      max-width: 480px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }}

    /* Header Profile Section */
    .profile-card {{
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      background: var(--card-bg);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid var(--card-border);
      border-radius: 28px;
      padding: 32px 24px 26px;
      box-shadow: var(--card-shadow);
      position: relative;
      overflow: hidden;
    }}

    .profile-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 6px;
      background: linear-gradient(90deg, var(--light-blue), var(--pastel-pink), var(--royal-blue), var(--light-blue));
    }}

    .avatar-wrapper {{
      position: relative;
      width: 116px;
      height: 116px;
      margin-bottom: 16px;
    }}

    .avatar-img {{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      object-position: center top;
      display: block;
      border: 4px solid var(--white);
      box-shadow: 0 10px 28px rgba(36, 63, 214, 0.22);
    }}

    .avatar-ring {{
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--light-blue), var(--royal-blue));
      z-index: -1;
    }}

    h1.brand-h1 {{
      font-size: 32px;
      font-weight: 900;
      letter-spacing: 2px;
      color: var(--royal-dark);
      margin-bottom: 4px;
    }}

    .full-name {{
      font-size: 19px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 6px;
    }}

    .tagline {{
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      color: var(--royal-blue);
      background: rgba(36, 63, 214, 0.08);
      padding: 6px 14px;
      border-radius: 999px;
      display: inline-block;
      margin-bottom: 14px;
    }}

    .bio {{
      font-size: 14.5px;
      font-weight: 500;
      color: var(--text-muted);
      line-height: 1.55;
      max-width: 390px;
      margin-bottom: 18px;
    }}

    /* Official Handle Banner */
    .handle-banner {{
      background: linear-gradient(135deg, rgba(174, 223, 242, 0.40), rgba(247, 200, 216, 0.35));
      border: 1px solid rgba(122, 160, 196, 0.40);
      border-radius: 14px;
      padding: 12px 18px;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
    }}

    .handle-banner .handle-text {{
      font-size: 19px;
      font-weight: 800;
      color: var(--royal-blue);
      text-decoration: underline;
      text-underline-offset: 5px;
      text-decoration-thickness: 2px;
      letter-spacing: 0.3px;
    }}

    /* Chapter Section Card */
    .chapter-card {{
      width: 100%;
      background: var(--card-bg);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid var(--card-border);
      border-radius: 22px;
      padding: 22px 20px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .chapter-pill-wrap {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}

    .chapter-pill {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: linear-gradient(135deg, var(--royal-blue), #1B3B8A);
      color: var(--white);
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 1px;
      padding: 6px 14px;
      border-radius: 999px;
      box-shadow: 0 4px 14px rgba(36, 63, 214, 0.28);
    }}

    .chapter-pill .dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #7ED6F8;
    }}

    .chapter-story {{
      font-size: 13.8px;
      color: #334E68;
      line-height: 1.58;
      font-weight: 500;
      text-align: center;
    }}

    /* Links Stack */
    .links-stack {{
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .link-card {{
      display: flex;
      align-items: center;
      gap: 14px;
      width: 100%;
      padding: 14px 18px;
      background: var(--card-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      box-shadow: var(--card-shadow);
      text-decoration: none;
      color: var(--text-main);
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}

    .link-card:hover, .link-card:focus-visible {{
      transform: translateY(-2px);
      box-shadow: var(--card-hover-shadow);
      border-color: #BEE3F8;
      background: rgba(255, 255, 255, 0.96);
      outline: none;
    }}

    .link-card:active {{
      transform: scale(0.985);
    }}

    .icon-box {{
      width: 44px;
      height: 44px;
      border-radius: 13px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
      overflow: hidden;
    }}

    .icon-box svg {{
      width: 23px;
      height: 23px;
    }}

    /* Platform icon stylings */
    .icon-ig {{
      background: linear-gradient(135deg, #F58529, #DD2A7B, #8134AF);
      color: #FFFFFF;
    }}

    .icon-fb {{
      background: #1877F2;
      color: #FFFFFF;
    }}

    .icon-tt {{
      background: #000000;
      color: #FFFFFF;
    }}

    .icon-yt {{
      background: #FF0000;
      color: #FFFFFF;
    }}

    .icon-xhs {{
      background: #FF2442;
      padding: 0;
    }}

    .icon-xhs img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      border-radius: 13px;
    }}

    .link-info {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 2px;
      min-width: 0;
    }}

    .link-label {{
      font-size: 16px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .link-subtitle {{
      font-size: 13px;
      font-weight: 500;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .link-arrow {{
      width: 20px;
      height: 20px;
      color: #94A3B8;
      flex-shrink: 0;
      transition: transform 0.2s ease, color 0.2s ease;
    }}

    .link-card:hover .link-arrow {{
      transform: translateX(3px);
      color: var(--royal-blue);
    }}

    /* About Section */
    .about-card {{
      width: 100%;
      background: var(--card-bg);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 20px 22px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .about-title {{
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--royal-blue);
      text-align: center;
    }}

    .about-body {{
      font-size: 13.8px;
      font-weight: 500;
      color: #334E68;
      line-height: 1.58;
    }}

    /* Footer */
    footer.page-footer {{
      width: 100%;
      text-align: center;
      padding: 12px 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 5px;
    }}

    .footer-line-1 {{
      font-size: 13.5px;
      font-weight: 700;
      color: var(--royal-dark);
    }}

    .footer-line-2 {{
      font-size: 12.5px;
      font-weight: 500;
      color: var(--text-muted);
    }}
  </style>
</head>
<body>

  <main class="container">
    
    <!-- Profile & Brand Hero Card -->
    <header class="profile-card">
      <div class="avatar-wrapper">
        <div class="avatar-ring"></div>
        <img src="data:image/jpeg;base64,{b64_img}" alt="Ryan Louie Nolasco" class="avatar-img">
      </div>
      
      <h1 class="brand-h1">RYAN</h1>
      <div class="full-name">Ryan Louie Nolasco</div>
      <div class="tagline">K-POP DANCE COVERS · OʻAHU, HAWAIʻI</div>
      
      <p class="bio">Dance reels, practice cuts &amp; polished covers — posted everywhere, same reel. New drops all through Chapter 2.</p>
      
      <div class="handle-banner">
        <span class="handle-text">@ryanlouienm</span>
      </div>
    </header>

    <!-- Chapter 2 Story Card -->
    <section class="chapter-card" aria-label="Chapter 2">
      <div class="chapter-pill-wrap">
        <div class="chapter-pill">
          <span class="dot"></span>
          <span>CHAPTER 2: PAINT THE WORLD</span>
        </div>
      </div>
      <p class="chapter-story">Chapter 1: Awakening The Ace came first. Now Chapter 2: Paint The World is about being fully yourself, no matter what. Hate is inevitable and will come regardless — but to put yourself out there, you must paint the world!</p>
    </section>

    <!-- Links Stack -->
    <nav class="links-stack" aria-label="Official Links">

      <!-- 1. Instagram -->
      <a href="https://www.instagram.com/ryanlouienm?xtok=Y25yaHUyZ3BseW43&amp;utm_source=qr" class="link-card" target="_blank" rel="noopener noreferrer">
        <div class="icon-box icon-ig">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
          </svg>
        </div>
        <div class="link-info">
          <span class="link-label">Instagram</span>
          <span class="link-subtitle">Reels, stories &amp; updates</span>
        </div>
        <svg class="link-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </a>

      <!-- 2. Facebook -->
      <a href="https://www.facebook.com/share/1JpFRVHH4j/?mibextid=wwXIfr" class="link-card" target="_blank" rel="noopener noreferrer">
        <div class="icon-box icon-fb">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
          </svg>
        </div>
        <div class="link-info">
          <span class="link-label">Facebook</span>
          <span class="link-subtitle">Reels, updates &amp; community posts</span>
        </div>
        <svg class="link-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </a>

      <!-- 3. TikTok -->
      <a href="https://www.tiktok.com/@ryanlouienm?_r=1&amp;_t=ZT-9AxGZhjOUbm" class="link-card" target="_blank" rel="noopener noreferrer">
        <div class="icon-box icon-tt">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64c.29 0 .58.04.86.11V9.38a6.34 6.34 0 0 0-.86-.06A6.34 6.34 0 0 0 3.1 15.66a6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.34-6.34V9.05a8.31 8.31 0 0 0 4.81 1.53v-3.5a4.84 4.84 0 0 1-1-.39z"/>
          </svg>
        </div>
        <div class="link-info">
          <span class="link-label">TikTok</span>
          <span class="link-subtitle">Daily dance TikToks</span>
        </div>
        <svg class="link-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </a>

      <!-- 4. YouTube -->
      <a href="https://youtube.com/@ryanlouienm?si=k9ac4z_xhN1ph43_" class="link-card" target="_blank" rel="noopener noreferrer">
        <div class="icon-box icon-yt">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
          </svg>
        </div>
        <div class="link-info">
          <span class="link-label">YouTube</span>
          <span class="link-subtitle">Shorts &amp; covers</span>
        </div>
        <svg class="link-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </a>

      <!-- 5. rednote 小红书 -->
      <a href="https://xhslink.cn/m/A94wY75Vcx1" class="link-card" target="_blank" rel="noopener noreferrer">
        <div class="icon-box icon-xhs">
          <img src="data:image/png;base64,{b64_xhs}" alt="rednote 小红书">
        </div>
        <div class="link-info">
          <span class="link-label">rednote 小红书</span>
          <span class="link-subtitle">Notes &amp; dance covers</span>
        </div>
        <svg class="link-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </a>

    </nav>

    <!-- About Ryan Card -->
    <section class="about-card" aria-label="About Ryan">
      <div class="about-title">About Ryan</div>
      <p class="about-body">Ryan is a boy dancer from Oʻahu who specializes in K-pop dance and performance — sharp, high-energy covers posted as simple reels, one track at a time.</p>
    </section>

    <!-- Footer -->
    <footer class="page-footer">
      <div class="footer-line-1">Check out Ryan's content!</div>
      <div class="footer-line-2">Tap a link above to watch on your favorite platform.</div>
    </footer>

  </main>

</body>
</html>
'''

with open('/Users/ryanlouienolasco/.gemini/antigravity/scratch/ryan-links/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated /Users/ryanlouienolasco/.gemini/antigravity/scratch/ryan-links/index.html successfully!")
