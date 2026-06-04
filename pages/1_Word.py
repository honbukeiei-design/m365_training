from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
from modules.training import page_header

st.set_page_config(page_title="Word Training", page_icon="📄", layout="wide")
st.markdown(f"<style>{Path('assets/style.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
page_header("📄", "Word：文書作成とクラウド保存", "リボンを切り替え、白紙ページ上で直接編集します。太字・下線・箇条書き・コメント・共有が画面に反映されます。")

word_html = r'''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<style>
*{box-sizing:border-box} body{margin:0;font-family:"Segoe UI",system-ui,"Yu Gothic",sans-serif;background:#f3f2f1;color:#242424}.word-shell{border:1px solid #c8c6c4;border-radius:14px;overflow:hidden;background:#fff;box-shadow:0 12px 30px rgba(0,0,0,.10)}.titlebar{height:42px;background:#2b579a;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 14px}.title-left{display:flex;align-items:center;gap:10px;font-weight:700}.file-name{font-size:14px;opacity:.95}.window-controls span{display:inline-flex;width:34px;height:26px;align-items:center;justify-content:center;border-radius:4px}.window-controls span:hover{background:rgba(255,255,255,.16)}.top-row{background:#fbfbfb;border-bottom:1px solid #d0d0d0;padding:8px 12px;display:flex;gap:8px;align-items:center}.quick{border:1px solid transparent;background:transparent;padding:6px 9px;border-radius:4px;cursor:pointer}.quick:hover{background:#edf3ff;border-color:#c7d7f5}.tabs{display:flex;gap:2px;background:#fff;border-bottom:1px solid #d0d0d0;padding:0 10px}.tab{border:0;background:transparent;padding:11px 16px 10px;cursor:pointer;font-weight:600;color:#323130;border-bottom:3px solid transparent}.tab:hover{background:#f3f2f1}.tab.active{color:#2b579a;border-bottom-color:#2b579a}.ribbon{background:#fdfdfd;border-bottom:1px solid #d0d0d0;min-height:110px;padding:10px 12px;display:flex;gap:10px;align-items:stretch;overflow:auto}.group{border-right:1px solid #e1dfdd;padding:0 12px 20px 0;min-width:125px;position:relative;display:flex;gap:6px;align-items:flex-start;flex-wrap:wrap}.group-label{position:absolute;bottom:0;left:0;right:12px;text-align:center;color:#605e5c;font-size:11px}.cmd{border:1px solid #d0d0d0;background:#fff;border-radius:5px;min-width:42px;height:38px;padding:4px 8px;cursor:pointer;font-weight:600}.cmd:hover{background:#edf3ff;border-color:#8ab4f8}.cmd.active{background:#deecff;border-color:#2b579a;color:#2b579a}.cmd.big{width:68px;height:62px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px}.cmd.big b{font-size:19px}.fontselect,.sizeselect{height:36px;border:1px solid #d0d0d0;border-radius:5px;background:white;padding:0 8px}.workspace{display:grid;grid-template-columns:1fr 300px;background:#f3f2f1;min-height:690px}.canvas-wrap{padding:34px 24px 60px;overflow:auto}.page{width:794px;min-height:1010px;margin:0 auto;background:white;border:1px solid #d0d0d0;box-shadow:0 4px 16px rgba(0,0,0,.18);padding:72px 82px;line-height:1.8;font-size:16px;outline:0}.page:focus{box-shadow:0 4px 18px rgba(43,87,154,.35)}.statusbar{height:30px;background:#f8f8f8;border-top:1px solid #d0d0d0;display:flex;align-items:center;justify-content:space-between;padding:0 12px;color:#605e5c;font-size:12px}.side{border-left:1px solid #d0d0d0;background:#faf9f8;padding:16px}.panel{background:#fff;border:1px solid #e1dfdd;border-radius:10px;padding:14px;margin-bottom:12px}.panel h3{margin:0 0 10px;font-size:16px}.badge{display:inline-flex;border-radius:999px;padding:4px 9px;background:#fff4ce;color:#8a4b00;font-weight:700;font-size:12px}.saved{background:#dff6dd;color:#107c10}.share-row{display:flex;align-items:center;justify-content:space-between;padding:8px;border-bottom:1px solid #f0f0f0}.comment{background:#fff4ce;border-bottom:2px solid #c19c00}.toast{position:fixed;right:24px;bottom:24px;background:#323130;color:#fff;padding:12px 16px;border-radius:8px;opacity:0;transform:translateY(10px);transition:.25s}.toast.show{opacity:1;transform:translateY(0)}.real-use{display:none;background:#e7f0ff;border:1px solid #b4d2ff;border-radius:12px;padding:14px;margin-top:12px}.real-use.show{display:block}.real-use a{display:inline-block;margin-top:8px;background:#2564cf;color:white;text-decoration:none;border-radius:8px;padding:9px 12px;font-weight:700}.hidden{display:none!important}
</style>
</head>
<body>
<div class="word-shell">
  <div class="titlebar"><div class="title-left"><span>📄 Word</span><span class="file-name" id="fileName">M365移行後のファイル保存ルール.docx</span></div><div class="window-controls"><span>—</span><span>□</span><span>×</span></div></div>
  <div class="top-row"><button class="quick" onclick="saveDoc()">💾 保存</button><button class="quick" onclick="undoCmd()">↶ 元に戻す</button><button class="quick" onclick="redoCmd()">↷ やり直し</button><span style="color:#605e5c;margin-left:auto" id="syncText">未保存の変更</span></div>
  <div class="tabs" id="tabs">
    <button class="tab active" data-tab="home">ホーム</button><button class="tab" data-tab="insert">挿入</button><button class="tab" data-tab="layout">レイアウト</button><button class="tab" data-tab="design">デザイン</button><button class="tab" data-tab="review">校閲</button><button class="tab" data-tab="view">表示</button><button class="tab" data-tab="mail">差し込み文書</button>
  </div>
  <div class="ribbon" id="ribbon"></div>
  <div class="workspace">
    <div class="canvas-wrap">
      <div id="page" class="page" contenteditable="true" spellcheck="false">
        <h1>Microsoft 365移行後のファイル保存ルール</h1>
        <p>旧Officeでは個人PCや共有フォルダーに保存していました。</p>
        <p>Microsoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。</p>
        <p>この白紙ページに自由に入力し、リボンから太字、下線、箇条書き、スタイル、コメント、共有を試してください。</p>
      </div>
    </div>
    <aside class="side">
      <div class="panel"><h3>ファイル状態</h3><span id="saveBadge" class="badge">未保存の変更</span><p style="font-size:13px;color:#605e5c">保存先：OneDrive - 個人</p></div>
      <div class="panel"><h3>共有</h3><div id="shareList"><div class="share-row"><span>自分のみ</span><span>🔒</span></div></div></div>
      <div class="panel"><h3>コメント</h3><div id="comments" style="font-size:13px;color:#605e5c">コメントはまだありません。</div></div>
      <div class="panel"><h3>操作ログ</h3><div id="log" style="font-size:13px;color:#605e5c">リボン操作を試してください。</div></div>
      <div id="realUse" class="real-use"><b>実際に使用してみよう</b><br><span>Word Onlineを開いて、同じ操作を本番環境で試せます。</span><br><a target="_blank" href="https://www.microsoft365.com/launch/word">実際のURLを開く</a></div>
    </aside>
  </div>
  <div class="statusbar"><span id="status">1ページ　日本語</span><span>ズーム 100%</span></div>
</div><div class="toast" id="toast"></div>
<script>
const page=document.getElementById('page');const ribbon=document.getElementById('ribbon');const log=document.getElementById('log');const toast=document.getElementById('toast');
function focusPage(){page.focus();}
function note(t){log.innerHTML='✓ '+t+'<br><span style="color:#8a8886">'+new Date().toLocaleTimeString('ja-JP')+'</span>';toast.textContent=t;toast.classList.add('show');setTimeout(()=>toast.classList.remove('show'),1400);document.getElementById('syncText').textContent='未保存の変更';document.getElementById('saveBadge').textContent='未保存の変更';document.getElementById('saveBadge').className='badge';}
function cmd(c,v=null){focusPage();document.execCommand(c,false,v);note('文書に「'+c+'」を反映しました');}
function saveDoc(){document.getElementById('syncText').textContent='OneDriveに保存済み';document.getElementById('saveBadge').textContent='保存済み';document.getElementById('saveBadge').className='badge saved';document.getElementById('realUse').classList.add('show');note('OneDriveに保存しました');}
function undoCmd(){cmd('undo')} function redoCmd(){cmd('redo')}
function setStyle(type){focusPage(); if(type==='title')document.execCommand('formatBlock',false,'H1'); if(type==='heading')document.execCommand('formatBlock',false,'H2'); if(type==='normal')document.execCommand('formatBlock',false,'P'); note('スタイルを適用しました');}
function addComment(){focusPage();let sel=window.getSelection();if(!sel.rangeCount || sel.toString()===''){note('コメントする文字列を選択してください');return;}let range=sel.getRangeAt(0);let span=document.createElement('span');span.className='comment';span.title='コメント: 共有前に表現を確認';range.surroundContents(span);document.getElementById('comments').innerHTML='<b>コメント1</b><br>「'+span.textContent+'」にコメントを追加しました。';note('コメントを追加しました');}
function shareDoc(){document.getElementById('shareList').innerHTML='<div class="share-row"><span>長野 太郎</span><span>編集可</span></div><div class="share-row"><span>組織内リンク</span><span>閲覧可</span></div>';document.getElementById('realUse').classList.add('show');note('共有設定を反映しました');}
function insertTable(){focusPage();document.execCommand('insertHTML',false,'<table border="1" style="border-collapse:collapse;width:100%;margin:12px 0"><tr><th>項目</th><th>保存先</th><th>共有方法</th></tr><tr><td>個人作業</td><td>OneDrive</td><td>指定ユーザー</td></tr><tr><td>チーム資料</td><td>SharePoint</td><td>Teams</td></tr></table>');note('表を挿入しました');}
function insertLink(){focusPage();document.execCommand('createLink',false,'https://www.microsoft365.com/');note('リンクを設定しました');}
function pageColor(c){page.style.background=c;note('ページ背景を変更しました');}
function setMargins(px){page.style.padding=px+'px';note('余白を変更しました');}
function setZoom(z){page.style.transform='scale('+z+')';page.style.transformOrigin='top center';document.getElementById('status').textContent='1ページ　ズーム '+Math.round(z*100)+'%';note('表示倍率を変更しました');}
function ribbonHome(){ribbon.innerHTML='<div class="group"><select class="fontselect" onchange="cmd(\'fontName\',this.value)"><option>Yu Gothic</option><option>Meiryo</option><option>MS Mincho</option></select><select class="sizeselect" onchange="cmd(\'fontSize\',this.value)"><option value="3">11</option><option value="4">14</option><option value="5">18</option><option value="6">24</option></select><button class="cmd" onclick="cmd(\'bold\')"><b>B</b></button><button class="cmd" onclick="cmd(\'underline\')"><u>U</u></button><button class="cmd" onclick="cmd(\'foreColor\',\'#c00000\')">A赤</button><div class="group-label">フォント</div></div><div class="group"><button class="cmd" onclick="cmd(\'insertUnorderedList\')">箇条書き</button><button class="cmd" onclick="cmd(\'justifyLeft\')">左</button><button class="cmd" onclick="cmd(\'justifyCenter\')">中央</button><button class="cmd" onclick="cmd(\'justifyRight\')">右</button><div class="group-label">段落</div></div><div class="group"><button class="cmd big" onclick="setStyle(\'title\')"><b>表題</b>タイトル</button><button class="cmd big" onclick="setStyle(\'heading\')"><b>見出し</b>H2</button><button class="cmd big" onclick="setStyle(\'normal\')"><b>標準</b>本文</button><div class="group-label">スタイル</div></div><div class="group"><button class="cmd big" onclick="addComment()"><b>💬</b>コメント</button><button class="cmd big" onclick="shareDoc()"><b>↗</b>共有</button><div class="group-label">共同作業</div></div>';}
function ribbonInsert(){ribbon.innerHTML='<div class="group"><button class="cmd big" onclick="insertTable()"><b>▦</b>表</button><button class="cmd big" onclick="document.execCommand(\'insertHorizontalRule\');note(\'区切り線を挿入しました\')"><b>—</b>区切り</button><button class="cmd big" onclick="document.execCommand(\'insertHTML\',false,\'<p>📌 アイコン付きメモ</p>\');note(\'アイコンを挿入しました\')"><b>📌</b>アイコン</button><button class="cmd big" onclick="insertLink()"><b>🔗</b>リンク</button><div class="group-label">挿入</div></div>';}
function ribbonLayout(){ribbon.innerHTML='<div class="group"><button class="cmd big" onclick="setMargins(54)"><b>狭い</b>余白</button><button class="cmd big" onclick="setMargins(82)"><b>標準</b>余白</button><button class="cmd big" onclick="setMargins(110)"><b>広い</b>余白</button><div class="group-label">ページ設定</div></div><div class="group"><button class="cmd" onclick="cmd(\'justifyLeft\')">左揃え</button><button class="cmd" onclick="cmd(\'justifyFull\')">両端揃え</button><div class="group-label">配置</div></div>';}
function ribbonDesign(){ribbon.innerHTML='<div class="group"><button class="cmd big" onclick="pageColor(\'#ffffff\')"><b>白</b>標準</button><button class="cmd big" onclick="pageColor(\'#fbf7ef\')"><b>淡黄</b>背景</button><button class="cmd big" onclick="pageColor(\'#f6fbff\')"><b>淡青</b>背景</button><button class="cmd big" onclick="page.style.border=\'2px solid #2b579a\';note(\'ページ罫線を設定しました\')"><b>□</b>罫線</button><div class="group-label">文書の書式設定</div></div>';}
function ribbonReview(){ribbon.innerHTML='<div class="group"><button class="cmd big" onclick="addComment()"><b>💬</b>コメント</button><button class="cmd big" onclick="document.execCommand(\'strikeThrough\');note(\'修正履歴風の取り消し線を反映しました\')"><b>S</b>変更</button><button class="cmd big" onclick="shareDoc()"><b>↗</b>共有</button><div class="group-label">校閲</div></div>';}
function ribbonView(){ribbon.innerHTML='<div class="group"><button class="cmd big" onclick="setZoom(0.85)"><b>85%</b>縮小</button><button class="cmd big" onclick="setZoom(1)"><b>100%</b>標準</button><button class="cmd big" onclick="setZoom(1.15)"><b>115%</b>拡大</button><div class="group-label">表示</div></div>';}
function ribbonMail(){ribbon.innerHTML='<div class="group"><button class="cmd big" onclick="document.execCommand(\'insertHTML\',false,\'<p>差し込み項目：«氏名» 様</p>\');note(\'差し込みフィールドを挿入しました\')"><b>«»</b>差し込み</button><button class="cmd big" onclick="document.execCommand(\'insertHTML\',false,\'<p>宛先リスト：部署別送付先</p>\');note(\'宛先リストを設定しました\')"><b>📇</b>宛先</button><div class="group-label">差し込み文書</div></div>';}
const maps={home:ribbonHome,insert:ribbonInsert,layout:ribbonLayout,design:ribbonDesign,review:ribbonReview,view:ribbonView,mail:ribbonMail};
document.querySelectorAll('.tab').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));b.classList.add('active');maps[b.dataset.tab]();note('「'+b.textContent+'」タブを表示しました');}));
page.addEventListener('input',()=>{document.getElementById('syncText').textContent='未保存の変更';document.getElementById('saveBadge').textContent='未保存の変更';document.getElementById('saveBadge').className='badge';});
ribbonHome();
</script>
</body></html>
'''
components.html(word_html, height=1000, scrolling=True)
