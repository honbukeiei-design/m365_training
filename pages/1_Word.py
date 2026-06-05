import streamlit as st
import streamlit.components.v1 as components
from modules.ui import load_css, page_header
from modules.urls import M365_URLS

st.set_page_config(page_title="Word Training", page_icon="📄", layout="wide")
load_css()
page_header("Word：文書作成とクラウド保存", "画面上部の指示に沿って、リボン・書式・コメント・共有・保存を順に体験します。")

word_url = M365_URLS["Word"]
html = f"""
<!doctype html><html lang='ja'><head><meta charset='utf-8'><style>
:root{{--blue:#185abd;--line:#c9d6e8;--bg:#e9edf5;--ribbon:#f7f9fc;--text:#1f2430;--muted:#697586;}}
*{{box-sizing:border-box}} body{{margin:0;font-family:'Segoe UI','Yu Gothic',Meiryo,sans-serif;background:linear-gradient(180deg,#e9eef7,#f7f8fb);color:var(--text)}}
.shell{{border:1px solid #c9d6e8;border-radius:20px;overflow:hidden;background:#fff;box-shadow:0 14px 38px rgba(22,36,70,.12)}}
.topbar{{height:42px;background:#174a7c;color:#fff;display:flex;align-items:center;gap:14px;padding:0 16px;font-size:14px}}
.logo{{font-weight:800;background:#0f6cbd;padding:6px 10px;border-radius:8px}} .docname{{font-weight:700}} .status{{margin-left:auto;opacity:.9}}
.taskbar{{background:#fff8e6;border-bottom:1px solid #ecd9a6;padding:14px 16px;display:flex;align-items:center;gap:14px}}
.tasktext{{font-weight:800;color:#684900}} .meter{{flex:1;height:10px;background:#eadfbf;border-radius:999px;overflow:hidden}} .meter span{{display:block;height:100%;width:0;background:#f59e0b;transition:.25s}}
.tabs{{display:flex;gap:4px;background:#f6f8fb;border-bottom:1px solid var(--line);padding:8px 12px 0}}
.tab{{border:0;background:transparent;padding:10px 16px;border-radius:8px 8px 0 0;font-weight:700;color:#26374f;cursor:pointer}}
.tab.active{{background:#fff;border:1px solid var(--line);border-bottom-color:#fff;color:#0f5db8}}
.ribbon{{min-height:88px;background:#fff;border-bottom:1px solid var(--line);padding:12px;display:flex;gap:10px;align-items:flex-start;flex-wrap:wrap}}
.group{{border-right:1px solid #d6dfec;padding-right:12px;margin-right:2px;min-height:58px}} .gtitle{{font-size:11px;color:#6b7280;text-align:center;margin-top:4px}}
.btn{{border:1px solid #c9d6e8;background:linear-gradient(#fff,#f1f5fb);border-radius:8px;padding:8px 10px;margin:2px;cursor:pointer;font-weight:650;box-shadow:0 1px 0 #fff inset}}
.btn:hover{{background:#eaf2ff;border-color:#78a7e8}} select,.miniinput{{border:1px solid #c9d6e8;border-radius:8px;padding:8px;background:white;margin:2px}}
.workspace{{display:grid;grid-template-columns:1fr 300px;gap:18px;padding:22px;background:#e9edf5}}
.pagewrap{{display:flex;justify-content:center;align-items:flex-start;min-height:780px}}
.page{{width:794px;min-height:1000px;background:white;border:1px solid #c7cfdb;box-shadow:0 10px 28px rgba(24,35,55,.18);padding:76px 82px;outline:none;line-height:1.8;font-size:16px;position:relative}}
.page:focus{{box-shadow:0 0 0 3px rgba(37,99,235,.18),0 10px 28px rgba(24,35,55,.18)}}
.page h1{{font-size:28px;margin:0 0 18px;color:#1d2738}} .page h2{{font-size:22px;color:#185abd;margin-top:24px}}
.panel{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px;box-shadow:0 8px 20px rgba(40,56,90,.08)}} .panel h3{{margin:0 0 10px;font-size:18px}}
.check{{display:flex;gap:8px;align-items:center;margin:9px 0;color:#475467}} .dot{{width:20px;height:20px;border:1px solid #c9d6e8;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:12px}}
.check.done .dot{{background:#1a7f37;color:white;border-color:#1a7f37}} .check.done{{color:#1a7f37;font-weight:700}}
.cta{{display:none;background:#ecfdf3;border:1px solid #86efac;border-radius:14px;padding:14px;margin-top:14px}} .cta a{{display:block;text-align:center;background:#185abd;color:#fff;text-decoration:none;border-radius:10px;padding:10px;margin-top:10px;font-weight:800}}
.savechip{{display:inline-block;background:#e7f5ea;color:#166534;border-radius:999px;padding:5px 10px;font-weight:800}} .comment{{background:#fff3cd;border-bottom:2px solid #facc15}}
.small{{font-size:12px;color:#697586}} .modal{{display:none;position:fixed;right:36px;top:210px;width:320px;background:#fff;border:1px solid #c9d6e8;border-radius:16px;box-shadow:0 18px 45px rgba(13,30,60,.25);padding:16px;z-index:5}}
</style></head><body>
<div class='shell'>
  <div class='topbar'><div class='logo'>W</div><div class='docname'>M365移行後の保存ルール.docx</div><div class='status' id='saveStatus'>未保存の変更</div></div>
  <div class='taskbar'><div class='tasktext' id='taskText'>体験 1/6：ホームタブで「太字」「下線」「箇条書き」を使ってください。</div><div class='meter'><span id='meter'></span></div></div>
  <div class='tabs' id='tabs'></div>
  <div class='ribbon' id='ribbon'></div>
  <div class='workspace'>
    <div class='pagewrap'><div class='page' contenteditable='true' id='doc'>
      <h1>M365移行後のファイル保存ルール</h1>
      <p>旧Officeでは個人PCや共有フォルダーに保存していました。Microsoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。</p>
      <h2>基本ルール</h2>
      <p>個人作業中の資料はOneDrive、チームで共有する正式資料はSharePointに保存します。</p>
      <p>この白紙ページ内をクリックして自由に編集できます。文字を選択してから太字や下線を押すと、選択範囲に反映されます。</p>
    </div></div>
    <div class='panel'><h3>体験チェック</h3>
      <div class='check' data-k='home'><span class='dot'>1</span>ホームの書式を使う</div>
      <div class='check' data-k='insert'><span class='dot'>2</span>挿入タブで表かリンクを追加</div>
      <div class='check' data-k='layout'><span class='dot'>3</span>レイアウトを変更</div>
      <div class='check' data-k='review'><span class='dot'>4</span>コメントを追加</div>
      <div class='check' data-k='share'><span class='dot'>5</span>共有範囲を確認</div>
      <div class='check' data-k='save'><span class='dot'>6</span>クラウド保存する</div>
      <div class='cta' id='cta'><b>体験完了です。</b><br>次は実際のWord for the webで同じ操作を試してください。<a href='{word_url}' target='_blank'>実体験をしてください：Wordを開く ↗</a><div class='small'>{word_url}</div></div>
    </div>
  </div>
</div>
<div class='modal' id='shareModal'><h3>共有</h3><p>共有範囲を選択しました。</p><button class='btn' onclick='closeShare()'>閉じる</button></div>
<script>
const tabs=['ホーム','挿入','レイアウト','デザイン','校閲','表示','差し込み文書'];
const done={{home:false,insert:false,layout:false,review:false,share:false,save:false}}; let active='ホーム';
const taskMap=[['home','体験 1/6：ホームタブで「太字」「下線」「箇条書き」を使ってください。'],['insert','体験 2/6：挿入タブで表またはリンクを追加してください。'],['layout','体験 3/6：レイアウトタブで余白や段組みを変更してください。'],['review','体験 4/6：校閲タブでコメントを追加してください。'],['share','体験 5/6：共有ボタンで共有範囲を確認してください。'],['save','体験 6/6：保存ボタンでクラウド保存を完了してください。']];
function mark(k){{done[k]=true;updateProgress();}}
function updateProgress(){{let n=Object.values(done).filter(Boolean).length; document.getElementById('meter').style.width=(n/6*100)+'%'; document.querySelectorAll('.check').forEach(c=>{{if(done[c.dataset.k])c.classList.add('done')}}); let next=taskMap.find(x=>!done[x[0]]); document.getElementById('taskText').textContent=next?next[1]:'体験完了：実体験URLから本物のWordを開いてください。'; if(n===6)document.getElementById('cta').style.display='block';}}
function cmd(c,v=null){{document.getElementById('doc').focus(); document.execCommand(c,false,v); mark('home');}}
function insertHTML(h){{document.getElementById('doc').focus(); document.execCommand('insertHTML',false,h); mark('insert');}}
function setTab(t){{active=t;drawTabs();drawRibbon();}}
function drawTabs(){{document.getElementById('tabs').innerHTML=tabs.map(t=>`<button class='tab ${{t===active?'active':''}}' onclick="setTab('${{t}}')">${{t}}</button>`).join('');}}
function drawRibbon(){{let r='';
 if(active==='ホーム') r=`<div class='group'><button class='btn' onclick="cmd('bold')"><b>B 太字</b></button><button class='btn' onclick="cmd('underline')"><u>U 下線</u></button><button class='btn' onclick="cmd('insertUnorderedList')">箇条書き</button><div class='gtitle'>フォント</div></div><div class='group'><select onchange="cmd('formatBlock',this.value)"><option value='p'>標準</option><option value='h1'>見出し1</option><option value='h2'>見出し2</option></select><button class='btn' onclick="cmd('justifyLeft')">左揃え</button><button class='btn' onclick="cmd('justifyCenter')">中央</button><div class='gtitle'>スタイル</div></div>`;
 if(active==='挿入') r=`<div class='group'><button class='btn' onclick="insertHTML('<table border=1 style=\\'border-collapse:collapse;width:100%;margin:12px 0\\'><tr><th>項目</th><th>保存先</th></tr><tr><td>個人作業</td><td>OneDrive</td></tr><tr><td>共有資料</td><td>SharePoint</td></tr></table>')">表</button><button class='btn' onclick="insertHTML('<a href=\\'{word_url}\\' target=\\'_blank\\'>Word for the web</a>')">リンク</button><button class='btn' onclick="insertHTML('<hr>')">区切り線</button><div class='gtitle'>挿入</div></div>`;
 if(active==='レイアウト') r=`<div class='group'><button class='btn' onclick="document.getElementById('doc').style.padding='58px 64px';mark('layout')">余白：狭い</button><button class='btn' onclick="document.getElementById('doc').style.padding='86px 96px';mark('layout')">余白：広い</button><button class='btn' onclick="document.getElementById('doc').style.columnCount=2;mark('layout')">2段組み</button><button class='btn' onclick="document.getElementById('doc').style.columnCount=1;mark('layout')">1段組み</button><div class='gtitle'>ページ設定</div></div>`;
 if(active==='デザイン') r=`<div class='group'><button class='btn' onclick="document.getElementById('doc').style.background='#fffef7';mark('layout')">ページ色</button><button class='btn' onclick="document.getElementById('doc').style.border='4px double #8aa6ca';mark('layout')">ページ罫線</button><button class='btn' onclick="document.getElementById('doc').style.fontFamily='Meiryo, sans-serif';mark('layout')">テーマ</button><div class='gtitle'>文書の書式設定</div></div>`;
 if(active==='校閲') r=`<div class='group'><button class='btn' onclick="document.getElementById('doc').focus();document.execCommand('insertHTML',false,'<span class=comment>コメント: 保存先を確認</span>');mark('review')">コメント</button><button class='btn' onclick="insertHTML('<p><b>変更履歴:</b> 保存先ルールを追記しました。</p>');mark('review')">変更履歴</button><div class='gtitle'>校閲</div></div>`;
 if(active==='表示') r=`<div class='group'><button class='btn' onclick="document.getElementById('doc').style.transform='scale(.9)';document.getElementById('doc').style.transformOrigin='top center'">90%</button><button class='btn' onclick="document.getElementById('doc').style.transform='scale(1)'">100%</button><button class='btn' onclick="document.getElementById('doc').style.transform='scale(1.1)';document.getElementById('doc').style.transformOrigin='top center'">110%</button><div class='gtitle'>ズーム</div></div>`;
 if(active==='差し込み文書') r=`<div class='group'><button class='btn' onclick="insertHTML('<p>宛先: 部署別研修対象者</p>')">宛先選択</button><button class='btn' onclick="insertHTML('<p>差し込みフィールド: {{部署名}}</p>')">フィールド挿入</button><div class='gtitle'>差し込み</div></div>`;
 r += `<div class='group'><button class='btn' onclick='share()'>共有</button><button class='btn' onclick='save()'>保存</button><div class='gtitle'>クラウド</div></div>`; document.getElementById('ribbon').innerHTML=r;}}
function share(){{mark('share');document.getElementById('shareModal').style.display='block';}}
function closeShare(){{document.getElementById('shareModal').style.display='none';}}
function save(){{mark('save');document.getElementById('saveStatus').innerHTML='<span class=savechip>OneDriveに保存済み</span>';}}
drawTabs();drawRibbon();updateProgress();
</script></body></html>
"""
components.html(html, height=1120, scrolling=True)
