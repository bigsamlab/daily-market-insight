fetch('data/reports.json').then(r=>r.json()).then(data=>{
const latest=document.getElementById('latest');
const list=document.getElementById('reports');
const arc=document.getElementById('archive');
if(data.length){
latest.innerHTML=`<h3>${data[0].date}</h3><a href="${data[0].url}">阅读日报</a>`;
}
data.forEach(r=>{
const li=document.createElement('li');
li.innerHTML=`<a href="${r.url}">${r.date}</a>`;
if(list) list.appendChild(li.cloneNode(true));
if(arc) arc.appendChild(li);
});
});
