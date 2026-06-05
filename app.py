from __future__ import annotations
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Microsoft 365 体験トレーニング", layout="wide", initial_sidebar_state="collapsed")

SERVICES = ["Word", "Excel", "Teams", "OneDrive", "SharePoint", "Copilot"]
SERVICE_URLS = {
    "Word": "https://word.cloud.microsoft/",
    "Excel": "https://excel.cloud.microsoft/",
    "Teams": "https://teams.microsoft.com/",
    "OneDrive": "https://onedrive.live.com/",
    "SharePoint": "https://www.microsoft.com/ja-jp/microsoft-365/sharepoint/collaboration/",
    "Copilot": "https://copilot.microsoft.com/",
}

CSS = """
<style>
[data-testid="stSidebar"], [data-testid="collapsedControl"] {display:none !important;}
.block-container{max-width:1240px;padding:18px 22px 36px 22px;}
.stApp{background:#f4f6fa;color:#111827;}
.main-header{border-bottom:4px solid #185abd;background:#ffffff;padding:18px 22px;margin:-18px -22px 18px -22px;}
.main-header h1{font-size:28px;margin:0 0 6px 0;font-weight:800;letter-spacing:.01em;}
.main-header p{font-size:14px;color:#606b7a;margin:0;}
.section-title{font-size:18px;font-weight:800;margin:16px 0 8px 0;}
div.stButton>button{border-radius:7px;border:1px solid #c7d2e5;background:#fff;color:#182233;font-weight:650;height:42px;}
div.stButton>button[kind="primary"]{background:#185abd;color:#fff;border-color:#185abd;}
.service-card{border:1px solid #d6dde9;background:#fff;border-radius:12px;padding:14px 16px;height:96px;box-shadow:0 2px 10px rgba(15,23,42,.04);}
.service-card strong{display:block;font-size:18px;margin-bottom:8px;}
.service-card span{color:#667085;font-size:13px;}
.open-card{border:1px solid #d6dde9;background:#fff;border-radius:10px;padding:12px;text-align:center;}
.small-note{font-size:13px;color:#667085;}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

if "service" not in st.session_state:
    st.session_state.service = "Word"

st.markdown("""
<div class="main-header">
  <h1>Microsoft 365 体験トレーニング</h1>
  <p>上部で体験するサービスを選択し、画面内のボタンや入力欄を操作します。操作結果は疑似画面に自動反映されます。</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">体験するサービスを選択</div>', unsafe_allow_html=True)
cols = st.columns(6)
for col, service in zip(cols, SERVICES):
    with col:
        st.markdown(f'<div class="service-card"><strong>{service}</strong><span>基本操作を体験</span></div>', unsafe_allow_html=True)
        if st.button("選択", key=f"select_{service}", type="primary" if st.session_state.service == service else "secondary", use_container_width=True):
            st.session_state.service = service
            st.rerun()


def shell_html(title: str, body: str, color: str = "#185abd", height: int = 780) -> str:
    return f"""
<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8" />
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#eef2f8;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Yu Gothic',Meiryo,sans-serif;color:#162033;}}
.app{{height:{height-5}px;border:1px solid #cbd5e1;border-radius:14px;overflow:hidden;background:#edf2fa;box-shadow:0 8px 22px rgba(15,23,42,.12)}}
.titlebar{{height:48px;background:{color};color:white;display:flex;align-items:center;gap:16px;padding:0 18px;font-weight:700;font-size:18px}}
.titlebar .doc{{opacity:.95;font-weight:650}}
.menubar{{height:42px;background:white;border-bottom:1px solid #d7deeb;display:flex;align-items:center;gap:18px;padding:0 18px;font-size:15px}}
.tab{{cursor:pointer;padding:10px 0;border-bottom:3px solid transparent}}
.tab.active{{color:{color};font-weight:700;border-bottom-color:{color}}}
.ribbon{{min-height:74px;background:#fbfcff;border-bottom:1px solid #d7deeb;padding:10px 16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
.group{{display:flex;gap:8px;align-items:center;border-right:1px solid #dbe2ee;padding-right:12px;margin-right:2px;min-height:44px}}
button,.btn,select,input{{font-family:inherit}}
button,.btn{{border:1px solid #c8d3e2;background:#fff;border-radius:6px;padding:7px 11px;cursor:pointer;font-size:14px;color:#172033}}
button:hover,.btn:hover{{background:#f2f6ff}}
button.on{{background:#e5efff;border-color:{color};color:{color};font-weight:700}}
select,input{{border:1px solid #c8d3e2;border-radius:6px;padding:7px 9px;background:white;font-size:14px}}
.train{{display:flex;justify-content:space-between;align-items:center;background:#f1f6ff;border:1px solid #bad3ff;border-radius:10px;margin:12px 18px;padding:11px 14px;font-size:14px}}
.train b{{color:#0b55c7}}
.workspace{{padding:22px;background:#e7edf7;min-height:560px;}}
.status{{height:30px;background:#f8fafc;border-top:1px solid #d7deeb;display:flex;justify-content:space-between;align-items:center;padding:0 16px;color:#4b5563;font-size:13px}}
.badge{{border-radius:999px;padding:4px 9px;background:#eff6ff;color:#174ea6;font-weight:650;font-size:12px}}
.done{{background:#f0fdf4;border:1px solid #b7e2c1;color:#14532d;border-radius:10px;padding:10px 12px;margin-left:8px}}
{body}
</style>
</head>
<body>
<div class="app">
"""


def word_component():
    html = shell_html("Word", """
.pagewrap{display:flex;justify-content:center;align-items:flex-start;height:528px;overflow:auto;padding-bottom:24px;}
.page{width:780px;min-height:930px;background:white;border:1px solid #d7dde8;box-shadow:0 12px 30px rgba(31,41,55,.18);padding:78px 88px;font-size:17px;line-height:1.9;outline:none;}
.page:focus{box-shadow:0 12px 30px rgba(31,41,55,.18),0 0 0 2px #8db3ff inset;}
.comment{border-left:4px solid #ffd84d;background:#fff8d6;padding:7px 10px;margin:14px 0;font-size:14px;}
table{border-collapse:collapse;margin:14px 0;width:100%;}td,th{border:1px solid #64748b;padding:7px;min-width:70px;}
body.design-blue .page{background:#f9fbff;border-color:#7aa6e8;}body.design-grid .page{background-image:linear-gradient(#eef2f8 1px, transparent 1px),linear-gradient(90deg,#eef2f8 1px,transparent 1px);background-size:22px 22px;}
    """, "#185abd", 820)
    html += r"""
<div class="titlebar"><span>Word</span><span class="doc">保存ルール.docx</span><span id="saveState" class="badge">自動保存 オン</span></div>
<div class="menubar" id="tabs">
  <span class="tab active" data-tab="file">ファイル</span><span class="tab" data-tab="home">ホーム</span><span class="tab" data-tab="insert">挿入</span><span class="tab" data-tab="layout">レイアウト</span><span class="tab" data-tab="design">デザイン</span><span class="tab" data-tab="review">校閲</span><span class="tab" data-tab="view">表示</span><span class="tab" data-tab="mail">差し込み文書</span>
</div>
<div class="ribbon" id="ribbon"></div>
<div class="train"><div><b>体験</b>：<span id="task">ホームで太字または下線を選び、白紙ページに反映してください。</span></div><div><b><span id="done">0</span>/8 完了</b></div></div>
<div class="workspace"><div class="pagewrap">
  <div id="page" class="page" contenteditable="true">
    <h2>M365移行後のファイル保存ルール</h2>
    <p>旧Officeでは個人PCや共有フォルダーに保存していました。</p>
    <p>Microsoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。</p>
  </div>
</div></div>
<div class="status"><span>ページ 1/1</span><span id="status">表示 100% ・ 標準余白 ・ 編集中</span></div>
</div>
<script>
const page=document.getElementById('page'), ribbon=document.getElementById('ribbon');
const tasks=['ホームで文字書式を選ぶ','挿入で表を追加する','レイアウトで余白を変更する','デザインで背景または罫線を選ぶ','校閲でコメントを入れる','表示でズームを変更する','差し込み文書でフィールドを入れる','ファイルで保存先と共有範囲を選ぶ'];
let done=new Set();
function mark(i){done.add(i);document.getElementById('done').textContent=done.size;document.getElementById('task').textContent=tasks.find((_,idx)=>!done.has(idx))||'体験完了。次は実サービスで同じ操作を試してください。'; if(done.size>=8){document.querySelector('.train').innerHTML='<div><b>体験完了</b>：基本操作を確認できました。下部の実サービスから同じ操作を試してください。</div><div class="done">完了</div>'}}
function exec(cmd,val=null){page.focus();document.execCommand(cmd,false,val);mark(0)}
function insertHTML(h,idx){page.focus();document.execCommand('insertHTML',false,h);mark(idx)}
function setTab(name){document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('active',t.dataset.tab===name)); render(name)}
document.getElementById('tabs').addEventListener('click',e=>{if(e.target.dataset.tab)setTab(e.target.dataset.tab)})
function render(tab){
 const R={
 file:`<div class="group"><span>保存先</span><select onchange="document.getElementById('saveState').textContent='保存先 '+this.value; mark(7)"><option>OneDrive - 個人</option><option>SharePoint - 部署サイト</option><option>Teams チャネル</option></select></div><div class="group"><span>共有</span><select onchange="insertHTML('<p><span class=badge>共有範囲：'+this.value+'</span></p>',7)"><option>自分のみ</option><option>指定したユーザー</option><option>組織内リンク</option></select></div>`,
 home:`<div class="group"><button onclick="exec('bold')">太字</button><button onclick="exec('underline')">下線</button><button onclick="exec('insertUnorderedList')">箇条書き</button></div><div class="group"><span>スタイル</span><select onchange="exec('formatBlock',this.value)"><option value='p'>標準</option><option value='h2'>見出し</option><option value='blockquote'>引用</option></select></div>`,
 insert:`<div class="group"><span>表</span><select onchange="if(this.value){let [r,c]=this.value.split('x');let h='<table>';for(let i=0;i<r;i++){h+='<tr>';for(let j=0;j<c;j++)h+='<td>セル</td>';h+='</tr>'}h+='</table>';insertHTML(h,1);this.value=''}"><option value=''>表サイズを選択</option><option value='2x2'>2×2</option><option value='3x3'>3×3</option><option value='4x3'>4×3</option></select></div><div class="group"><button onclick="insertHTML('<p><a href=https://word.cloud.microsoft/>Word for the web</a></p>',1)">リンク</button></div>`,
 layout:`<div class="group"><span>余白</span><select onchange="page.style.padding=this.value;document.getElementById('status').textContent='表示 100% ・ 余白変更済み ・ 編集中';mark(2)"><option value='78px 88px'>標準</option><option value='52px 62px'>狭い</option><option value='100px 110px'>広い</option></select></div>`,
 design:`<div class="group"><span>ページ背景</span><select onchange="document.body.className=this.value;mark(3)"><option value=''>白</option><option value='design-blue'>薄い青</option><option value='design-grid'>グリッド</option></select></div><div class="group"><span>罫線</span><select onchange="page.style.border=this.value;mark(3)"><option value='1px solid #d7dde8'>標準</option><option value='4px double #185abd'>二重線</option><option value='3px solid #64748b'>実線</option></select></div>`,
 review:`<div class="group"><input id='commentText' placeholder='コメントを入力' onkeydown="if(event.key==='Enter'){addComment()}"><button onclick="addComment()">コメント</button></div>`,
 view:`<div class="group"><span>ズーム</span><select onchange="page.style.transform='scale('+this.value+')';page.style.transformOrigin='top center';document.getElementById('status').textContent='表示 '+Math.round(this.value*100)+'% ・ 編集中';mark(5)"><option value='1'>100%</option><option value='0.85'>85%</option><option value='1.15'>115%</option></select></div>`,
 mail:`<div class="group"><span>差し込みフィールド</span><select onchange="if(this.value){insertHTML('<span class=badge>«'+this.value+'»</span>',6);this.value=''}"><option value=''>選択</option><option>宛名</option><option>所属</option><option>日付</option></select></div>`
 }; ribbon.innerHTML=R[tab];
}
function addComment(){let v=document.getElementById('commentText').value||'確認してください';insertHTML('<div class="comment">コメント：'+v+'</div>',4)}
render('file');
</script>
</body></html>"""
    components.html(html, height=820, scrolling=False)


def excel_component():
    html = shell_html("Excel", """
.workspace{height:590px;overflow:auto}.grid{border-collapse:collapse;background:white;width:900px;box-shadow:0 10px 25px rgba(15,23,42,.12)}.grid th{background:#f3f6f9;border:1px solid #cbd5e1;text-align:center;padding:7px;font-weight:600}.grid td{border:1px solid #cbd5e1;width:120px;height:38px;padding:6px}.grid td[contenteditable='true']:focus{outline:3px solid #107c41;background:#eefaf2}.fx{background:white;border:1px solid #cbd5e1;border-radius:8px;padding:8px 10px;display:flex;gap:10px;align-items:center;margin:0 18px 10px 18px}.chart{margin-top:18px;width:460px;height:170px;border-left:1px solid #94a3b8;border-bottom:1px solid #94a3b8;display:flex;align-items:flex-end;gap:22px;padding:12px}.bar{background:#107c41;width:44px;color:white;text-align:center;font-size:12px;display:flex;align-items:flex-end;justify-content:center;padding-bottom:4px}
    """, "#107c41", 820)
    html += r"""
<div class="titlebar"><span>Excel</span><span class="doc">売上一覧.xlsx</span><span class="badge">自動保存 オン</span></div>
<div class="menubar" id="tabs"><span class="tab active" data-tab="home">ホーム</span><span class="tab" data-tab="insert">挿入</span><span class="tab" data-tab="formula">数式</span><span class="tab" data-tab="data">データ</span><span class="tab" data-tab="view">表示</span></div>
<div class="ribbon" id="ribbon"></div>
<div class="train"><div><b>体験</b>：<span id="task">セルを選択し、数式バーで =SUM(B2:B4) を試してください。</span></div><div><b><span id="done">0</span>/6 完了</b></div></div>
<div class="fx"><b>fx</b><input id="formula" style="width:520px" value="=SUM(B2:B4)" onkeydown="if(event.key==='Enter')calcFormula()"><button onclick="calcFormula()">Enter</button><span id="fxmsg" class="small"></span></div>
<div class="workspace"><table class="grid" id="grid"></table><div id="chart"></div></div>
<div class="status"><span>シート1</span><span id="status">準備完了</span></div></div>
<script>
let done=new Set(), selected='B5'; const tasks=['数式バーでSUMを計算する','ホームでセル書式を変更する','挿入で表またはグラフを追加する','数式で平均や最大値を試す','データでフィルターを使う','表示倍率を変更する'];
const data={A1:'月',B1:'売上',A2:'4月',B2:'120',A3:'5月',B3:'180',A4:'6月',B4:'240',A5:'合計',B5:''};
function mark(i){done.add(i);document.getElementById('done').textContent=done.size;document.getElementById('task').textContent=tasks.find((_,idx)=>!done.has(idx))||'体験完了。下部の実サービスで同じ操作を試してください。'}
function addr(c,r){return String.fromCharCode(64+c)+r}
function renderGrid(){let h='<tr><th></th>';for(let c=1;c<=6;c++)h+='<th>'+String.fromCharCode(64+c)+'</th>';h+='</tr>';for(let r=1;r<=10;r++){h+='<tr><th>'+r+'</th>';for(let c=1;c<=6;c++){let a=addr(c,r);h+=`<td contenteditable="true" data-a="${a}" class="${a===selected?'sel':''}">${data[a]||''}</td>`}h+='</tr>'}document.getElementById('grid').innerHTML=h;document.querySelectorAll('td').forEach(td=>{td.onclick=()=>{selected=td.dataset.a;document.getElementById('formula').value=data[selected]||'';renderGrid()};td.oninput=()=>{data[td.dataset.a]=td.textContent}})}
function rangeVals(rng){let [s,e]=rng.split(':');let c=s[0], r1=+s.slice(1), r2=+e.slice(1);let vals=[];for(let r=r1;r<=r2;r++){vals.push(parseFloat(data[c+r]||0)||0)}return vals}
function calcFormula(){let f=document.getElementById('formula').value.toUpperCase().replaceAll(' ','');let m=f.match(/^=(SUM|AVERAGE|MAX|MIN)\(([A-Z][0-9]+:[A-Z][0-9]+)\)$/);if(!m){document.getElementById('fxmsg').textContent='対応例：=SUM(B2:B4)';return}let vals=rangeVals(m[2]);let res=m[1]==='SUM'?vals.reduce((a,b)=>a+b,0):m[1]==='AVERAGE'?Math.round(vals.reduce((a,b)=>a+b,0)/vals.length*10)/10:m[1]==='MAX'?Math.max(...vals):Math.min(...vals);data[selected]=res;renderGrid();document.getElementById('fxmsg').textContent=selected+' に '+res+' を表示';mark(m[1]==='SUM'?0:3)}
function setTab(name){document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('active',t.dataset.tab===name));renderRibbon(name)}
document.getElementById('tabs').onclick=e=>{if(e.target.dataset.tab)setTab(e.target.dataset.tab)};
function renderRibbon(tab){const R={home:`<div class="group"><button onclick="document.querySelector('[data-a='+selected+']').style.fontWeight='700';mark(1)">太字</button><button onclick="document.querySelector('[data-a='+selected+']').style.background='#fff2cc';mark(1)">塗りつぶし</button><button onclick="document.querySelector('[data-a='+selected+']').style.border='2px solid #107c41';mark(1)">罫線</button></div>`,insert:`<div class="group"><button onclick="insertTable()">テーブル化</button><button onclick="insertChart()">グラフ</button></div>`,formula:`<div class="group"><button onclick="document.getElementById('formula').value='=SUM(B2:B4)';calcFormula()">SUM</button><button onclick="document.getElementById('formula').value='=AVERAGE(B2:B4)';calcFormula()">AVERAGE</button><button onclick="document.getElementById('formula').value='=MAX(B2:B4)';calcFormula()">MAX</button></div>`,data:`<div class="group"><button onclick="document.getElementById('status').textContent='フィルターが有効です';mark(4)">フィルター</button><button onclick="document.getElementById('status').textContent='並べ替え：売上降順';mark(4)">並べ替え</button></div>`,view:`<div class="group"><span>表示倍率</span><select onchange="document.getElementById('grid').style.transform='scale('+this.value+')';document.getElementById('grid').style.transformOrigin='top left';mark(5)"><option value='1'>100%</option><option value='0.85'>85%</option><option value='1.15'>115%</option></select></div>`};document.getElementById('ribbon').innerHTML=R[tab]}
function insertTable(){document.getElementById('grid').style.border='3px solid #107c41';document.getElementById('status').textContent='範囲 A1:B5 をテーブル化しました';mark(2)}
function insertChart(){let vals=[+data.B2,+data.B3,+data.B4];let max=Math.max(...vals);let h='<div class="chart">';vals.forEach((v,i)=>h+=`<div class=bar style="height:${30+v/max*120}px">${v}</div>`);h+='</div>';document.getElementById('chart').innerHTML=h;mark(2)}
renderGrid();renderRibbon('home');
</script></body></html>"""
    components.html(html, height=820, scrolling=False)


def teams_component():
    html = shell_html("Teams", """
.teams{display:grid;grid-template-columns:230px 1fr;height:560px}.rail{background:#f7f7fc;border-right:1px solid #dde0f2;padding:16px}.chat{background:white;padding:16px;display:flex;flex-direction:column}.thread{flex:1;overflow:auto}.msg{background:#f2f3f8;border-radius:12px;padding:9px 12px;margin:8px 0;max-width:78%}.me{background:#e9e7ff;margin-left:auto}.mention{color:#5b5fc7;font-weight:800}.compose{display:flex;gap:8px;border-top:1px solid #e5e7eb;padding-top:10px}.compose input{flex:1}.channel{padding:9px;border-radius:7px}.channel.active{background:#e8e8f7;font-weight:700}
    """, "#464775", 780)
    html += r"""
<div class="titlebar"><span>Teams</span><span class="doc">一般チャネル</span></div>
<div class="ribbon"><div class="group"><button onclick="shareFile()">ファイル共有</button><button onclick="react()">リアクション</button><button onclick="meet()">会議開始</button></div></div>
<div class="train"><div><b>体験</b>：<span id="task">@メンションを付けてメッセージを送信してください。</span></div><div><b><span id="done">0</span>/4 完了</b></div></div>
<div class="teams"><div class="rail"><b>チーム</b><div class="channel active">総務・経営企画</div><div class="channel">医療情報</div><div class="channel">研修</div></div><div class="chat"><div class="thread" id="thread"><div class="msg"><b>佐藤</b><br>移行後の保存ルールを確認しましょう。</div></div><div class="compose"><input id="msg" value="@田中 さん、資料を確認してください"><button onclick="send()">送信</button></div></div></div>
<div class="status"><span>チャット・ファイル・会議</span><span id="status">準備完了</span></div></div>
<script>
let done=new Set();const tasks=['@メンションを付けて送信する','ファイルを共有する','リアクションを付ける','会議を開始する'];function mark(i){done.add(i);document.getElementById('done').textContent=done.size;document.getElementById('task').textContent=tasks.find((_,idx)=>!done.has(idx))||'体験完了。下部の実サービスで同じ操作を試してください。'}
function send(){let v=document.getElementById('msg').value;let html=v.replace(/@\S+/g,m=>'<span class=mention>'+m+'</span>');document.getElementById('thread').innerHTML+=`<div class="msg me"><b>あなた</b><br>${html}</div>`;if(v.includes('@'))mark(0);document.getElementById('msg').value=''}
function shareFile(){document.getElementById('thread').innerHTML+='<div class="msg me"><b>あなた</b><br>ファイルを共有しました：保存ルール.docx</div>';mark(1)}
function react(){document.getElementById('thread').innerHTML+='<div class="msg">佐藤の投稿に「いいね」を付けました。</div>';mark(2)}
function meet(){document.getElementById('status').textContent='会議を開始しました';document.getElementById('thread').innerHTML+='<div class="msg me"><b>会議</b><br>今すぐ会議を開始しました。</div>';mark(3)}
</script></body></html>"""
    components.html(html, height=780, scrolling=False)


def simple_component(name: str, color: str, actions: list[str]):
    buttons = ''.join([f"<button onclick=\"doAction('{a}',{i})\">{a}</button>" for i, a in enumerate(actions)])
    html = shell_html(name, """
.panel{background:white;border:1px solid #d7deeb;border-radius:12px;padding:18px;min-height:410px;box-shadow:0 8px 22px rgba(15,23,42,.08)}.row{display:flex;gap:10px;margin:10px 0}.item{border:1px solid #d7deeb;border-radius:8px;padding:12px;background:#fafcff}.log{margin-top:14px;border-left:4px solid #185abd;background:#f1f6ff;padding:10px}
    """, color, 700)
    html += f"""
<div class="titlebar"><span>{name}</span><span class="doc">基本操作</span></div>
<div class="ribbon"><div class="group">{buttons}</div></div>
<div class="train"><div><b>体験</b>：<span id="task">{actions[0]} を試してください。</span></div><div><b><span id="done">0</span>/{len(actions)} 完了</b></div></div>
<div class="workspace"><div class="panel"><h2>{name} 体験画面</h2><div class="row"><div class="item">研修資料.docx</div><div class="item">売上一覧.xlsx</div><div class="item">共有フォルダー</div></div><div id="log" class="log">操作結果がここに表示されます。</div></div></div>
<div class="status"><span>{name}</span><span>準備完了</span></div></div>
<script>
let done=new Set();const actions={actions!r};function doAction(a,i){{done.add(i);document.getElementById('done').textContent=done.size;document.getElementById('log').innerHTML=a+' を実行しました。UI上の状態を更新しました。';document.getElementById('task').textContent=actions.find((_,idx)=>!done.has(idx))||'体験完了。下部の実サービスで同じ操作を試してください。';}}
</script></body></html>"""
    components.html(html, height=700, scrolling=False)

st.markdown("---")
if st.session_state.service == "Word":
    word_component()
elif st.session_state.service == "Excel":
    excel_component()
elif st.session_state.service == "Teams":
    teams_component()
elif st.session_state.service == "OneDrive":
    simple_component("OneDrive", "#0364b8", ["ファイルをアップロード", "共有リンクを作成", "同期状態を確認", "バージョン履歴から復元"])
elif st.session_state.service == "SharePoint":
    simple_component("SharePoint", "#036c70", ["サイトを選択", "ドキュメントを開く", "権限を確認", "ニュースを投稿"])
else:
    simple_component("Copilot", "#0f6cbd", ["依頼文を入力", "要約を作成", "文章を整える", "次の操作を提案"])

st.markdown('<div class="section-title">実サービス</div>', unsafe_allow_html=True)
open_cols = st.columns(6)
for c, name in zip(open_cols, SERVICES):
    with c:
        st.markdown(f'<div class="open-card"><strong>{name}</strong></div>', unsafe_allow_html=True)
        st.link_button("開く", SERVICE_URLS[name], use_container_width=True)
