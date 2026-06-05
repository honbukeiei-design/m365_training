import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Microsoft 365 体験トレーニング", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"], [data-testid="stSidebarNav"], header, footer {display:none !important;}
.block-container{padding:0 !important; max-width:100% !important;}
[data-testid="stAppViewContainer"]{background:#f3f6fb;}
iframe{display:block; width:100%; border:0;}
</style>
""", unsafe_allow_html=True)

HTML = r'''
<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
:root{
  --blue:#185abd; --blue2:#0f6cbd; --excel:#107c41; --teams:#6264a7; --onedrive:#0078d4; --sp:#03787c; --copilot:#5b5fc7;
  --bg:#f3f6fb; --panel:#ffffff; --line:#d7e0ef; --text:#172033; --muted:#667085; --soft:#eef4ff;
  --shadow:0 12px 28px rgba(25,54,95,.12);
}
*{box-sizing:border-box}
body{margin:0; font-family:"Segoe UI", "Noto Sans JP", system-ui, sans-serif; color:var(--text); background:var(--bg); font-size:15px;}
.app-shell{max-width:1480px; margin:0 auto; padding:16px 18px 28px;}
.hub-title{font-size:24px; font-weight:800; margin:0 0 12px;}
.service-tabs{display:grid; grid-template-columns:repeat(6,1fr); gap:10px; margin-bottom:14px;}
.service-tab{border:1px solid #c7d4e8; background:#fff; color:#0c244a; border-radius:8px; height:42px; font-weight:700; cursor:pointer; transition:.15s;}
.service-tab:hover{background:#f6f9ff; border-color:#8fb4ee;}
.service-tab.active{background:#2563d6; color:#fff; border-color:#2563d6; box-shadow:0 5px 14px rgba(37,99,214,.22);}
.training-tip{display:flex; justify-content:space-between; gap:20px; align-items:center; margin:12px 0 14px; padding:12px 16px; border:1px solid #9ec3ff; background:#edf5ff; border-radius:10px; color:#0b356b;}
.training-tip b{color:#0057c2}.complete{font-weight:800; color:#0057c2; white-space:nowrap}
.m365-frame{background:#fff; border:1px solid #cad6e8; border-radius:12px; overflow:hidden; box-shadow:var(--shadow);}
.titlebar{height:52px; display:flex; align-items:center; padding:0 22px; color:#fff; font-weight:800; font-size:20px; gap:18px;}
.titlebar.word{background:#185abd}.titlebar.excel{background:#107c41}.titlebar.teams{background:#6264a7}.titlebar.onedrive{background:#0078d4}.titlebar.sharepoint{background:#03787c}.titlebar.copilot{background:#5b5fc7}
.app-name{font-size:21px}.doc-name{opacity:.95}.window-actions{margin-left:auto; opacity:.9; font-size:13px; display:flex; gap:14px}
.ribbon-tabs{display:flex; gap:2px; background:#fff; border-bottom:1px solid var(--line); padding:0 10px; height:44px; align-items:end;}
.ribbon-tab{height:38px; min-width:96px; border:0; background:transparent; border-radius:7px 7px 0 0; font-weight:700; cursor:pointer; color:#12213b;}
.ribbon-tab.active{background:#edf4ff; color:#004aa8; border:1px solid #c6d7f2; border-bottom-color:#edf4ff;}
.ribbon{min-height:76px; padding:12px 16px; display:flex; gap:12px; align-items:center; background:#fbfcff; border-bottom:1px solid var(--line);}
.group{display:flex; align-items:center; gap:8px; padding-right:14px; border-right:1px solid #d9e2f1; min-height:44px;}
.group:last-child{border-right:0}.label{font-size:12px; color:var(--muted)}
.btn, .tool-btn, select, input, textarea{font-family:inherit; font-size:14px;}
.btn,.tool-btn{border:1px solid #bdd0eb; background:#fff; color:#0c244a; border-radius:7px; padding:8px 13px; cursor:pointer; min-height:36px;}
.btn:hover,.tool-btn:hover{background:#f0f6ff; border-color:#7ea7e9}.tool-btn.active{background:#dbeafe; color:#004aa8; border-color:#7ea7e9; font-weight:800}
select,input,textarea{border:1px solid #c7d4e8; background:#fff; border-radius:7px; padding:8px 10px; color:#12213b;}
.workspace{background:#e8eef8; padding:22px 24px 18px; min-height:560px;}
.statusbar{height:32px; padding:7px 18px; background:#f8fbff; border-top:1px solid var(--line); color:#536078; display:flex; gap:22px; font-size:13px;}
/* Word */
.word-stage{display:grid; grid-template-columns:minmax(680px,1fr) 290px; gap:18px; align-items:start;}
.paper-wrap{display:flex; justify-content:center}.paper{width:760px; min-height:850px; background:#fff; border:1px solid #d4dce9; box-shadow:0 10px 34px rgba(18,42,78,.18); padding:92px 86px; line-height:1.75; font-size:16px; outline:none;}
.paper:focus{box-shadow:0 0 0 2px #9ec3ff, 0 10px 34px rgba(18,42,78,.18)}
.paper h2{font-size:20px; margin:0 0 8px}.paper.border{border:4px double #4472c4}.paper.bluebg{background:#f2f7ff}.paper.narrow{padding:62px 56px}.paper.wide{padding:112px 110px}.paper .commented{background:#fff3cd; border-bottom:2px solid #d99e00}.paper .field{background:#e7f0ff; border:1px dashed #2b67c9; padding:1px 5px}
.side-pane{background:#fff; border:1px solid var(--line); border-radius:10px; padding:14px; box-shadow:0 8px 22px rgba(25,54,95,.07)}
.side-pane h3{margin:0 0 10px; font-size:16px}.info-row{display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #eef2f8}.info-row:last-child{border-bottom:0}.badge{display:inline-block; background:#e8f2ff; color:#0057c2; border:1px solid #b7d2ff; border-radius:999px; padding:3px 8px; font-size:12px; font-weight:700}.note{background:#f7faff; border-left:4px solid #2b67c9; padding:10px; margin-top:10px; color:#263850}
/* Excel */
.excel-area{background:#fff; border:1px solid var(--line); box-shadow:0 10px 28px rgba(20,64,42,.12)}
.formula-bar{display:grid; grid-template-columns:56px 1fr 110px; gap:8px; padding:9px; background:#f6faf7; border-bottom:1px solid var(--line); align-items:center}.fx{font-weight:800;color:#107c41;text-align:center}.grid{width:100%; border-collapse:collapse; table-layout:fixed}.grid th,.grid td{border:1px solid #dce5ef; height:38px; padding:5px 8px; background:#fff}.grid th{background:#eef5ef; color:#174b2f; font-weight:700;text-align:center}.grid .rowh{width:46px;background:#eef5ef;text-align:center;font-weight:700}.grid td{outline:none}.grid td.selected{box-shadow:inset 0 0 0 2px #107c41;background:#f2fff6}.grid td.bold{font-weight:800}.grid td.underline{text-decoration:underline}.grid td.fill{background:#fff2cc}.chart-box{height:190px; margin:14px; border:1px solid #d7e0ef; display:flex; align-items:end; gap:20px; padding:20px; background:#fbfdff}.bar{width:54px;background:#107c41;border-radius:4px 4px 0 0;position:relative}.bar span{position:absolute;bottom:-24px;width:80px;left:-12px;text-align:center;font-size:12px}
/* Teams */
.teams-shell{display:grid; grid-template-columns:250px 1fr 290px; min-height:560px; background:#fff; border:1px solid var(--line); border-radius:10px; overflow:hidden}.teams-left{background:#f4f4fb; border-right:1px solid #dddff5; padding:12px}.team-item{padding:10px;border-radius:8px;margin-bottom:6px}.team-item.active{background:#e6e6fa;color:#37398f;font-weight:800}.chat-main{display:flex; flex-direction:column}.chat-header{padding:14px 18px;border-bottom:1px solid var(--line);font-weight:800}.chat-list{flex:1;padding:18px;background:#fbfbff}.message{max-width:78%; background:#fff;border:1px solid #e1e4f4;border-radius:10px;padding:9px 12px;margin-bottom:10px;box-shadow:0 2px 8px rgba(20,20,80,.05)}.message.me{margin-left:auto;background:#f0f2ff}.mention{color:#5b5fc7;font-weight:800}.compose{padding:12px;border-top:1px solid var(--line);display:grid;grid-template-columns:1fr auto;gap:8px}.teams-side{background:#fbfbff;border-left:1px solid var(--line);padding:14px}.file-chip{border:1px solid #d7d9f2;background:#fff;border-radius:8px;padding:9px;margin:8px 0}
/* OneDrive / SharePoint */
.file-ui{display:grid;grid-template-columns:220px 1fr 300px; min-height:560px; background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden}.file-nav{background:#f8fbff;border-right:1px solid var(--line);padding:12px}.nav-item{padding:10px;border-radius:8px;margin-bottom:4px}.nav-item.active{background:#e8f2ff;color:#0057c2;font-weight:800}.file-main{padding:16px}.commandbar{display:flex;gap:8px;margin-bottom:12px;align-items:center}.file-table{width:100%;border-collapse:collapse}.file-table th,.file-table td{border-bottom:1px solid #eef2f8;padding:10px;text-align:left}.file-table th{color:#536078;font-size:12px;background:#fbfdff}.file-row{cursor:pointer}.file-row:hover,.file-row.selected{background:#eef6ff}.details{background:#fbfdff;border-left:1px solid var(--line);padding:16px}.progress{height:7px;background:#d7e6ff;border-radius:999px;overflow:hidden;margin:8px 0}.progress div{height:100%;background:#0f6cbd}.news-card{border:1px solid #d7e0ef;border-radius:9px;padding:10px;margin-top:8px;background:#fff}.site-banner{height:96px;background:linear-gradient(135deg,#03787c,#0f6cbd);border-radius:10px;color:#fff;padding:22px;font-size:22px;font-weight:800;margin-bottom:12px}
/* Copilot */
.copilot-shell{display:grid;grid-template-columns:290px 1fr;min-height:560px;background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden}.copilot-left{background:#f7f7ff;border-right:1px solid var(--line);padding:14px}.prompt-card{border:1px solid #dadaf3;border-radius:10px;background:#fff;padding:10px;margin:8px 0;cursor:pointer}.prompt-card:hover{background:#f0f0ff}.copilot-main{padding:20px}.prompt-box{width:100%;height:130px;resize:vertical}.answer{margin-top:14px;border:1px solid #dadaf3;border-radius:12px;background:#fbfbff;padding:16px;min-height:180px}.answer h3{margin-top:0}.source-row{display:flex;gap:8px;margin:10px 0}.source-pill{border:1px solid #c7d4e8;border-radius:999px;padding:6px 10px;background:#fff}
.external{margin-top:14px;background:#fff;border:1px solid #d4deed;border-radius:10px;padding:14px}.external h2{margin:0 0 10px;font-size:18px}.external-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}.external a{text-align:center;text-decoration:none;border:1px solid #c7d4e8;border-radius:8px;padding:10px;background:#fff;color:#073763;font-weight:700}.external a:hover{background:#f0f6ff;border-color:#7ea7e9}
.hidden{display:none !important}.small{font-size:12px;color:var(--muted)}
@media(max-width:1000px){.service-tabs,.external-grid{grid-template-columns:repeat(2,1fr)}.word-stage,.teams-shell,.file-ui,.copilot-shell{grid-template-columns:1fr}.details,.teams-side{border-left:0;border-top:1px solid var(--line)}.paper{width:100%;padding:48px 34px}.workspace{padding:14px}}
</style>
</head>
<body>
<div class="app-shell">
  <h1 class="hub-title">Microsoft 365 体験トレーニング</h1>
  <div class="service-tabs" id="serviceTabs"></div>
  <div id="trainingTip" class="training-tip"></div>
  <div id="appArea"></div>
  <div class="external">
    <h2>実サービス</h2>
    <div class="external-grid">
      <a target="_blank" rel="noopener" href="https://word.cloud.microsoft/">Word を開く</a>
      <a target="_blank" rel="noopener" href="https://excel.cloud.microsoft/">Excel を開く</a>
      <a target="_blank" rel="noopener" href="https://teams.microsoft.com/">Teams を開く</a>
      <a target="_blank" rel="noopener" href="https://onedrive.live.com/">OneDrive を開く</a>
      <a target="_blank" rel="noopener" href="https://www.microsoft.com/microsoft-365/sharepoint/collaboration">SharePoint を開く</a>
      <a target="_blank" rel="noopener" href="https://copilot.microsoft.com/">Copilot を開く</a>
    </div>
  </div>
</div>
<script>
const services = ["Word","Excel","Teams","OneDrive","SharePoint","Copilot"];
const colors = {Word:"word", Excel:"excel", Teams:"teams", OneDrive:"onedrive", SharePoint:"sharepoint", Copilot:"copilot"};
let currentService = "Word";
let state = {
  Word:{tab:"ホーム", done:new Set(), bold:false, underline:false, bullets:false, style:"標準", margin:"標準", bg:false, border:false, zoom:"100%", saved:"未保存", share:"未共有", comments:[]},
  Excel:{tab:"ホーム", done:new Set(), selected:"B2", formula:"", protected:false, chart:false, cells:{B2:120,B3:180,B4:240,C2:"外来",C3:"病棟",C4:"健診",D2:0,D3:0,D4:0,D5:""}},
  Teams:{done:new Set(), messages:[{who:"佐藤",text:"会議資料を確認お願いします。"}], files:[], meeting:false, reaction:false},
  OneDrive:{done:new Set(), selected:"研修資料.docx", uploaded:false, shared:false, synced:false, restored:false, files:["研修資料.docx","売上一覧.xlsx","共有フォルダー"]},
  SharePoint:{done:new Set(), site:"総務課サイト", added:false, permission:false, news:false, files:["保存ルール.docx","職員向け手順.xlsx","研修資料.pdf"]},
  Copilot:{done:new Set(), prompt:"", answer:""}
};
const steps = {
 Word:["白紙ページの本文を編集","ホームで文字書式を選ぶ","挿入で表を入れる","レイアウトで余白を変える","デザインで背景または罫線を変更","校閲でコメントを付ける","表示でズームを変える","ファイルで保存先を選ぶ","共有範囲を選ぶ"],
 Excel:["セルを選択して値を編集","数式バーに =SUM(B2:B4) を入力","ホームで書式を変更","挿入でグラフを表示","表示倍率を変更","シートを保護する"],
 Teams:["@メンションを付けて送信","ファイルを共有","リアクションを付ける","会議を開始"],
 OneDrive:["ファイルをアップロード","共有リンクを作成","同期状態を確認","バージョン履歴から復元"],
 SharePoint:["サイトを選択","ドキュメントを追加","権限を確認","ニュースを投稿"],
 Copilot:["プロンプトを入力","要約を作成","文章を整える","次の操作を提案"]
};
function doneCount(s){return state[s].done.size}
function mark(s, label){state[s].done.add(label); render();}
function nextStep(s){return steps[s].find(x=>!state[s].done.has(x)) || "体験完了。下部の実サービスで同じ操作を試してください。"}
function renderTabs(){
  document.getElementById('serviceTabs').innerHTML = services.map(s=>`<button class="service-tab ${s===currentService?'active':''}" onclick="currentService='${s}';render()">${s}</button>`).join('');
}
function renderTip(){
  const n=doneCount(currentService), total=steps[currentService].length;
  document.getElementById('trainingTip').innerHTML = `<div><b>体験：</b>${nextStep(currentService)}</div><div class="complete">${n}/${total} 完了</div>`;
}
function render(){renderTabs(); renderTip(); document.getElementById('appArea').innerHTML = views[currentService](); afterRender();}
function ribbonTabs(service, tabs){ const st=state[service]; return `<div class="ribbon-tabs">${tabs.map(t=>`<button class="ribbon-tab ${st.tab===t?'active':''}" onclick="state['${service}'].tab='${t}'; render()">${t}</button>`).join('')}</div>`}
function title(service, name){return `<div class="titlebar ${colors[service]}"><span class="app-name">${service}</span><span class="doc-name">${name}</span><span class="window-actions">自動保存　共有　コメント</span></div>`}
function wordRibbon(){
 const w=state.Word; const tab=w.tab;
 if(tab==='ホーム') return `<div class="ribbon"><div class="group"><button class="tool-btn ${w.bold?'active':''}" onclick="state.Word.bold=!state.Word.bold; mark('Word','ホームで文字書式を選ぶ')">太字</button><button class="tool-btn ${w.underline?'active':''}" onclick="state.Word.underline=!state.Word.underline; mark('Word','ホームで文字書式を選ぶ')">下線</button><button class="tool-btn ${w.bullets?'active':''}" onclick="state.Word.bullets=!state.Word.bullets; mark('Word','ホームで文字書式を選ぶ')">箇条書き</button></div><div class="group"><span class="label">スタイル</span><select onchange="state.Word.style=this.value; mark('Word','ホームで文字書式を選ぶ')"><option ${w.style==='標準'?'selected':''}>標準</option><option ${w.style==='見出し 1'?'selected':''}>見出し 1</option><option ${w.style==='強調'?'selected':''}>強調</option></select></div></div>`;
 if(tab==='挿入') return `<div class="ribbon"><div class="group"><span class="label">表</span><button class="btn" onclick="insertWordTable(2,3); mark('Word','挿入で表を入れる')">2行×3列</button><button class="btn" onclick="insertWordTable(3,3); mark('Word','挿入で表を入れる')">3行×3列</button></div><div class="group"><button class="btn" onclick="insertAtCursor('<a href=#>参考リンク</a>'); mark('Word','挿入で表を入れる')">リンク</button></div></div>`;
 if(tab==='レイアウト') return `<div class="ribbon"><div class="group"><span class="label">余白</span><select onchange="state.Word.margin=this.value; mark('Word','レイアウトで余白を変える')"><option ${w.margin==='標準'?'selected':''}>標準</option><option ${w.margin==='狭い'?'selected':''}>狭い</option><option ${w.margin==='広い'?'selected':''}>広い</option></select></div></div>`;
 if(tab==='デザイン') return `<div class="ribbon"><div class="group"><button class="tool-btn ${w.bg?'active':''}" onclick="state.Word.bg=!state.Word.bg; mark('Word','デザインで背景または罫線を変更')">ページ背景</button><button class="tool-btn ${w.border?'active':''}" onclick="state.Word.border=!state.Word.border; mark('Word','デザインで背景または罫線を変更')">ページ罫線</button></div></div>`;
 if(tab==='校閲') return `<div class="ribbon"><div class="group"><input id="commentInput" placeholder="コメント内容" value="確認をお願いします"><button class="btn" onclick="addComment(); mark('Word','校閲でコメントを付ける')">コメント追加</button></div></div>`;
 if(tab==='表示') return `<div class="ribbon"><div class="group"><span class="label">ズーム</span><select onchange="state.Word.zoom=this.value; mark('Word','表示でズームを変える')"><option>90%</option><option selected>100%</option><option>120%</option></select></div></div>`;
 if(tab==='ファイル') return `<div class="ribbon"><div class="group"><span class="label">保存先</span><select onchange="state.Word.saved=this.value; mark('Word','ファイルで保存先を選ぶ')"><option>未保存</option><option>OneDrive - 個人</option><option>SharePoint - 総務課サイト</option></select></div><div class="group"><span class="label">共有</span><select onchange="state.Word.share=this.value; mark('Word','共有範囲を選ぶ')"><option>未共有</option><option>自分のみ</option><option>指定したユーザー</option><option>組織内リンク</option></select></div></div>`;
 return `<div class="ribbon"><div class="group"><button class="btn" onclick="insertAtCursor('<span class=field>氏名</span>'); mark('Word','共有範囲を選ぶ')">差し込みフィールド：氏名</button><button class="btn" onclick="insertAtCursor('<span class=field>部署</span>')">部署</button></div></div>`;
}
function wordPageHTML(){
 const w=state.Word; let cls=['paper']; if(w.bg)cls.push('bluebg'); if(w.border)cls.push('border'); if(w.margin==='狭い')cls.push('narrow'); if(w.margin==='広い')cls.push('wide');
 let style=`transform:scale(${w.zoom==='90%'?.9:w.zoom==='120%'?1.2:1}); transform-origin:top center;`;
 let pcls=[]; if(w.bold)pcls.push('font-weight:800'); if(w.underline)pcls.push('text-decoration:underline');
 return `<div id="wordPaper" class="${cls.join(' ')}" style="${style}" contenteditable="true" oninput="mark('Word','白紙ページの本文を編集')">
 <h2 contenteditable="true">M365移行後のファイル保存ルール</h2>
 <p style="${pcls.join(';')}">${w.bullets?'・ ':''}旧Officeでは個人PCや共有フォルダーに保存していました。</p>
 <p style="${pcls.join(';')}">${w.bullets?'・ ':''}Microsoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。</p>
 </div>`;
}
const views={
 Word:()=>`${title('Word','保存ルール.docx')}${ribbonTabs('Word',['ファイル','ホーム','挿入','レイアウト','デザイン','校閲','表示','差し込み文書'])}${wordRibbon()}<div class="workspace"><div class="word-stage"><div class="paper-wrap">${wordPageHTML()}</div><div class="side-pane"><h3>文書の状態</h3><div class="info-row"><span>保存先</span><b>${state.Word.saved}</b></div><div class="info-row"><span>共有</span><b>${state.Word.share}</b></div><div class="info-row"><span>表示</span><b>${state.Word.zoom}</b></div><div class="info-row"><span>コメント</span><b>${state.Word.comments.length} 件</b></div><div class="note">白紙ページを直接編集し、リボン操作の結果がこの画面に反映されます。</div>${state.Word.comments.map(c=>`<div class="note">コメント：${c}</div>`).join('')}</div></div></div><div class="statusbar"><span>ページ 1/1</span><span>表示 ${state.Word.zoom}</span><span>${state.Word.saved}</span></div>`,
 Excel:()=>`${title('Excel','売上一覧.xlsx')}${ribbonTabs('Excel',['ホーム','挿入','数式','データ','表示','校閲'])}${excelRibbon()}<div class="workspace"><div class="excel-area"><div class="formula-bar"><div class="fx">fx</div><input id="formulaInput" value="${state.Excel.formula}" placeholder="=SUM(B2:B4)" onkeydown="if(event.key==='Enter'){applyFormula(this.value)}"><button class="btn" onclick="applyFormula(document.getElementById('formulaInput').value)">計算</button></div>${excelGrid()}${state.Excel.chart?chartHTML():''}</div></div><div class="statusbar"><span>選択セル ${state.Excel.selected}</span><span>${state.Excel.protected?'保護中':'編集可能'}</span></div>`,
 Teams:()=>`${title('Teams','総務課 チャネル')}${teamsRibbon()}<div class="workspace"><div class="teams-shell"><div class="teams-left"><b>チーム</b><div class="team-item active">総務課</div><div class="team-item">病院連携</div><div class="team-item">情報共有</div></div><div class="chat-main"><div class="chat-header">一般</div><div class="chat-list" id="chatList">${state.Teams.messages.map(m=>`<div class="message ${m.who==='自分'?'me':''}"><b>${m.who}</b><br>${m.text.replace(/@[\w一-龠ぁ-んァ-ヶ]+/g,'<span class=mention>$&</span>')}</div>`).join('')}</div><div class="compose"><input id="teamMessage" value="@佐藤 研修資料を共有します。" placeholder="@名前 を付けてメッセージ"><button class="btn" onclick="sendTeams()">送信</button></div></div><div class="teams-side"><h3>共有ファイル</h3>${state.Teams.files.map(f=>`<div class="file-chip">${f}</div>`).join('')||'<p class="small">まだ共有ファイルはありません。</p>'}<h3>状態</h3><p>${state.Teams.reaction?'リアクション済み':'リアクション未実施'}</p><p>${state.Teams.meeting?'会議中':'会議未開始'}</p></div></div></div>`,
 OneDrive:()=>`${title('OneDrive','自分のファイル')}${oneDriveRibbon()}<div class="workspace"><div class="file-ui"><div class="file-nav"><div class="nav-item active">自分のファイル</div><div class="nav-item">共有</div><div class="nav-item">最近使用した項目</div><div class="nav-item">ごみ箱</div></div><div class="file-main"><div class="commandbar"><button class="btn" onclick="uploadOneDrive()">アップロード</button><button class="btn" onclick="state.OneDrive.shared=true; mark('OneDrive','共有リンクを作成')">リンクを作成</button><button class="btn" onclick="state.OneDrive.synced=true; mark('OneDrive','同期状態を確認')">同期を確認</button><button class="btn" onclick="state.OneDrive.restored=true; mark('OneDrive','バージョン履歴から復元')">復元</button></div>${fileTable('OneDrive')}</div><div class="details">${oneDriveDetails()}</div></div></div>`,
 SharePoint:()=>`${title('SharePoint','総務課サイト')}${sharePointRibbon()}<div class="workspace"><div class="file-ui"><div class="file-nav"><div class="nav-item active">ホーム</div><div class="nav-item">ドキュメント</div><div class="nav-item">ページ</div><div class="nav-item">サイトの内容</div></div><div class="file-main"><div class="site-banner">${state.SharePoint.site}</div><div class="commandbar"><select onchange="state.SharePoint.site=this.value; mark('SharePoint','サイトを選択')"><option>総務課サイト</option><option>研修サイト</option><option>情報共有サイト</option></select><button class="btn" onclick="addSharePointDoc()">ドキュメントを追加</button><button class="btn" onclick="state.SharePoint.permission=true; mark('SharePoint','権限を確認')">権限を確認</button><button class="btn" onclick="state.SharePoint.news=true; mark('SharePoint','ニュースを投稿')">ニュースを投稿</button></div>${fileTable('SharePoint')}${state.SharePoint.news?'<div class="news-card"><b>ニュース</b><br>Microsoft 365移行後の保存ルールを公開しました。</div>':''}</div><div class="details">${sharePointDetails()}</div></div></div>`,
 Copilot:()=>`${title('Copilot','基本操作')}${copilotRibbon()}<div class="workspace"><div class="copilot-shell"><div class="copilot-left"><b>プロンプト例</b><div class="prompt-card" onclick="setPrompt('この研修資料.docxを3行で要約してください。')">資料を要約</div><div class="prompt-card" onclick="setPrompt('職員向けに、OneDriveとSharePointの使い分けを分かりやすく説明してください。')">文章を作成</div><div class="prompt-card" onclick="setPrompt('次に確認すべきMicrosoft 365移行作業を箇条書きで提案してください。')">次の操作を提案</div><div class="source-row"><span class="source-pill">研修資料.docx</span></div><div class="source-row"><span class="source-pill">売上一覧.xlsx</span></div></div><div class="copilot-main"><h2>Copilotに依頼する</h2><textarea id="copilotPrompt" class="prompt-box" placeholder="ここにプロンプトを入力してください">${state.Copilot.prompt}</textarea><br><br><button class="btn" onclick="runCopilot('要約を作成')">要約を作成</button> <button class="btn" onclick="runCopilot('文章を整える')">文章を整える</button> <button class="btn" onclick="runCopilot('次の操作を提案')">次の操作を提案</button><div class="answer"><h3>回答</h3>${state.Copilot.answer || 'プロンプトを入力してボタンを押すと、回答がここに表示されます。'}</div></div></div></div>`
};
function excelRibbon(){const e=state.Excel; if(e.tab==='ホーム')return `<div class="ribbon"><div class="group"><button class="tool-btn" onclick="toggleCellClass('bold'); mark('Excel','ホームで書式を変更')">太字</button><button class="tool-btn" onclick="toggleCellClass('underline'); mark('Excel','ホームで書式を変更')">下線</button><button class="tool-btn" onclick="toggleCellClass('fill'); mark('Excel','ホームで書式を変更')">塗りつぶし</button></div></div>`; if(e.tab==='挿入')return `<div class="ribbon"><div class="group"><button class="btn" onclick="state.Excel.chart=true; mark('Excel','挿入でグラフを表示')">棒グラフ</button></div></div>`; if(e.tab==='数式')return `<div class="ribbon"><div class="group"><button class="btn" onclick="state.Excel.formula='=SUM(B2:B4)'; applyFormula(state.Excel.formula)">SUM</button><button class="btn" onclick="state.Excel.formula='=AVERAGE(B2:B4)'; applyFormula(state.Excel.formula)">AVERAGE</button></div></div>`; if(e.tab==='表示')return `<div class="ribbon"><div class="group"><button class="btn" onclick="mark('Excel','表示倍率を変更')">表示倍率 100%</button><button class="btn" onclick="mark('Excel','表示倍率を変更')">枠線</button></div></div>`; if(e.tab==='校閲')return `<div class="ribbon"><div class="group"><button class="btn" onclick="state.Excel.protected=true; mark('Excel','シートを保護する')">シート保護</button></div></div>`; return `<div class="ribbon"><div class="group"><button class="btn" onclick="mark('Excel','セルを選択して値を編集')">フィルター</button><button class="btn" onclick="mark('Excel','セルを選択して値を編集')">並べ替え</button></div></div>`}
function excelGrid(){let rows=['1','2','3','4','5'];let cols=['A','B','C','D']; let h='<table class="grid"><tr><th></th>'+cols.map(c=>`<th>${c}</th>`).join('')+'</tr>'; rows.forEach(r=>{h+=`<tr><th class="rowh">${r}</th>`; cols.forEach(c=>{let cell=c+r; let val=cell==='A1'?'月':cell==='B1'?'売上':cell==='C1'?'区分':cell==='D1'?'集計':(state.Excel.cells[cell]??''); h+=`<td contenteditable="true" id="cell-${cell}" class="${state.Excel.selected===cell?'selected':''}" onclick="state.Excel.selected='${cell}'; render()" oninput="state.Excel.cells['${cell}']=this.innerText; mark('Excel','セルを選択して値を編集')">${val}</td>`});h+='</tr>'});return h+'</table>'}
function chartHTML(){return `<div class="chart-box"><div class="bar" style="height:80px"><span>B2</span></div><div class="bar" style="height:120px"><span>B3</span></div><div class="bar" style="height:160px"><span>B4</span></div></div>`}
function teamsRibbon(){return `<div class="ribbon"><div class="group"><button class="btn" onclick="shareTeamsFile()">ファイル共有</button><button class="btn" onclick="state.Teams.reaction=true; mark('Teams','リアクションを付ける')">リアクション</button><button class="btn" onclick="state.Teams.meeting=true; mark('Teams','会議を開始')">会議開始</button></div></div>`}
function oneDriveRibbon(){return `<div class="ribbon"><div class="group"><button class="btn" onclick="uploadOneDrive()">アップロード</button><button class="btn" onclick="state.OneDrive.shared=true; mark('OneDrive','共有リンクを作成')">共有</button><button class="btn" onclick="state.OneDrive.synced=true; mark('OneDrive','同期状態を確認')">同期</button></div></div>`}
function sharePointRibbon(){return `<div class="ribbon"><div class="group"><button class="btn" onclick="addSharePointDoc()">新規</button><button class="btn" onclick="state.SharePoint.permission=true; mark('SharePoint','権限を確認')">アクセス許可</button><button class="btn" onclick="state.SharePoint.news=true; mark('SharePoint','ニュースを投稿')">ニュース</button></div></div>`}
function copilotRibbon(){return `<div class="ribbon"><div class="group"><button class="btn" onclick="setPrompt('この資料の要点を3つにまとめてください。')">依頼文を入力</button><button class="btn" onclick="runCopilot('要約を作成')">要約</button><button class="btn" onclick="runCopilot('文章を整える')">整える</button><button class="btn" onclick="runCopilot('次の操作を提案')">提案</button></div></div>`}
function fileTable(s){let arr=s==='OneDrive'?state.OneDrive.files:state.SharePoint.files;return `<table class="file-table"><tr><th>名前</th><th>更新日時</th><th>共有</th><th>状態</th></tr>${arr.map(f=>`<tr class="file-row ${(state[s].selected||'')===f?'selected':''}" onclick="state['${s}'].selected='${f}'; render()"><td>${f}</td><td>今日</td><td>${(s==='OneDrive'&&state.OneDrive.shared)?'リンクあり':'-'}</td><td>${(s==='OneDrive'&&state.OneDrive.synced)?'同期済み':'最新'}</td></tr>`).join('')}</table>`}
function oneDriveDetails(){const o=state.OneDrive;return `<h3>詳細</h3><div class="info-row"><span>選択</span><b>${o.selected}</b></div><div class="info-row"><span>共有</span><b>${o.shared?'リンク作成済み':'未共有'}</b></div><div class="info-row"><span>同期</span><b>${o.synced?'同期済み':'未確認'}</b></div><div class="info-row"><span>復元</span><b>${o.restored?'前の版を復元':'未実施'}</b></div><div class="progress"><div style="width:${o.uploaded?100:35}%"></div></div><p class="small">操作結果がファイル一覧と詳細ペインに反映されます。</p>`}
function sharePointDetails(){const s=state.SharePoint;return `<h3>サイト情報</h3><div class="info-row"><span>サイト</span><b>${s.site}</b></div><div class="info-row"><span>権限</span><b>${s.permission?'閲覧/編集を確認済み':'未確認'}</b></div><div class="info-row"><span>ニュース</span><b>${s.news?'投稿済み':'未投稿'}</b></div><p class="small">部門・チームで共有する文書は、SharePointのサイトとライブラリで管理します。</p>`}
function afterRender(){}
function insertAtCursor(html){document.getElementById('wordPaper')?.focus(); document.execCommand('insertHTML',false,html)}
function insertWordTable(r,c){let html='<table style="border-collapse:collapse;width:100%;margin:14px 0">';for(let i=0;i<r;i++){html+='<tr>';for(let j=0;j<c;j++)html+='<td style="border:1px solid #333;padding:8px">項目</td>';html+='</tr>'}html+='</table>';insertAtCursor(html)}
function addComment(){let v=document.getElementById('commentInput')?.value||'確認をお願いします';state.Word.comments.push(v)}
function applyFormula(v){state.Excel.formula=v; let nums=[Number(state.Excel.cells.B2)||0,Number(state.Excel.cells.B3)||0,Number(state.Excel.cells.B4)||0]; let res=''; let up=v.toUpperCase(); if(up.includes('SUM'))res=nums.reduce((a,b)=>a+b,0); else if(up.includes('AVERAGE'))res=Math.round(nums.reduce((a,b)=>a+b,0)/nums.length*10)/10; else if(up.includes('MAX'))res=Math.max(...nums); else if(up.includes('MIN'))res=Math.min(...nums); state.Excel.cells.D5=res; mark('Excel','数式バーに =SUM(B2:B4) を入力')}
function toggleCellClass(cls){setTimeout(()=>{let el=document.getElementById('cell-'+state.Excel.selected); if(el)el.classList.toggle(cls)},0)}
function sendTeams(){let v=document.getElementById('teamMessage').value; state.Teams.messages.push({who:'自分',text:v}); if(v.includes('@'))mark('Teams','@メンションを付けて送信'); else render();}
function shareTeamsFile(){state.Teams.files.push('研修資料.docx'); mark('Teams','ファイルを共有')}
function uploadOneDrive(){if(!state.OneDrive.files.includes('アップロード資料.docx'))state.OneDrive.files.push('アップロード資料.docx'); state.OneDrive.selected='アップロード資料.docx'; state.OneDrive.uploaded=true; mark('OneDrive','ファイルをアップロード')}
function addSharePointDoc(){if(!state.SharePoint.files.includes('新規共有手順.docx'))state.SharePoint.files.push('新規共有手順.docx'); state.SharePoint.selected='新規共有手順.docx'; mark('SharePoint','ドキュメントを追加')}
function setPrompt(p){state.Copilot.prompt=p; mark('Copilot','プロンプトを入力')}
function runCopilot(kind){let p=document.getElementById('copilotPrompt')?.value || state.Copilot.prompt; state.Copilot.prompt=p; if(!p.trim()){state.Copilot.answer='先にプロンプトを入力してください。'; render(); return;} let body=''; if(kind==='要約を作成')body='要約：\n1. 個人作業はOneDriveへ保存します。\n2. 部門共有はSharePointで管理します。\n3. 関係者への連絡や共同作業はTeamsから行います。'; else if(kind==='文章を整える')body='整えた文章：\nMicrosoft 365移行後は、文書の目的に応じてOneDriveとSharePointを使い分け、Teamsで関係者へ共有します。'; else body='次の操作提案：\n・保存先を確認する\n・共有範囲を指定する\n・Teamsで関係者にメンションする'; state.Copilot.answer=`<p><b>入力した依頼：</b>${p}</p><pre style="white-space:pre-wrap;font-family:inherit">${body}</pre>`; mark('Copilot',kind)}
render();
</script>
</body>
</html>
'''
components.html(HTML, height=1050, scrolling=True)
