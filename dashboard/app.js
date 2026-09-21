async function load(){const rows=await(await fetch('../data/processed/nongshim_dashboard.json')).json();const r=rows.at(-1);
const f=(v)=>v==null?'—':Number(v).toLocaleString('ko-KR',{maximumFractionDigits:2});
const cards=[['매출',f(r.sales)],['영업이익률',f(r.operating_margin_pct)+'%'],['순이익률',f(r.net_margin_pct)+'%'],['ROE',f(r.roe_pct)+'%'],['부채비율',f(r.debt_ratio_pct)+'%'],['FCF',f(r.fcf)]];
document.querySelector('#cards').innerHTML=cards.map(x=>`<div class="card">${x[0]}<b>${x[1]}</b></div>`).join('');
const c=['year','sales_growth_pct','operating_margin_pct','net_margin_pct','debt_ratio_pct','equity_ratio_pct','cfo_to_net_income_pct','roa_pct','roe_pct','fcf'];
const l=['연도','매출성장률','영업이익률','순이익률','부채비율','자기자본비율','CFO/순이익','ROA','ROE','FCF'];
document.querySelector('#table').innerHTML='<tr>'+l.map(x=>`<th>${x}</th>`).join('')+'</tr>'+rows.map(x=>'<tr>'+c.map((k,i)=>`<td>${i?f(x[k]):x[k]}${i&&k.endsWith('_pct')?'%':''}</td>`).join('')+'</tr>').join('');}load();