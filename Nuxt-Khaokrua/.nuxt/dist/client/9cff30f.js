(window.webpackJsonp=window.webpackJsonp||[]).push([[9],{443:function(t,e,r){var content=r(451);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,r(8).default)("161f5656",content,!0,{sourceMap:!1})},450:function(t,e,r){"use strict";r(443)},451:function(t,e,r){(e=r(7)(!1)).push([t.i,".card-popup[data-v-e42c49fa]{border-radius:10px}.title-popup span[data-v-e42c49fa]{margin:30px;font-size:30px;font-weight:700}.div-action[data-v-e42c49fa]{width:60%;padding:20px}",""]),t.exports=e},462:function(t,e,r){"use strict";var n={name:"popup"},o=(r(450),r(29)),c=r(30),d=r.n(c),l=r(425),v=r(411),f=r(263),m=r(477),x=r(481),component=Object(o.a)(n,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"popup-container"},[r("v-dialog",{attrs:{"max-width":"290"},model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[r("v-card",[r("v-card-title",{staticClass:"headline"},[t._v("\n        Use Google's location service?\n      ")]),t._v(" "),r("v-card-text",[t._v("\n        Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.\n      ")]),t._v(" "),r("v-card-actions",[r("v-spacer"),t._v(" "),r("v-btn",{attrs:{color:"green darken-1",text:""},on:{click:function(e){t.dialog=!1}}},[t._v("\n          Disagree\n        ")]),t._v(" "),r("v-btn",{attrs:{color:"green darken-1",text:""},on:{click:function(e){t.dialog=!1}}},[t._v("\n          Agree\n        ")])],1)],1)],1)],1)}),[],!1,null,"e42c49fa",null);e.a=component.exports;d()(component,{VBtn:l.a,VCard:v.a,VCardActions:f.a,VCardText:f.b,VCardTitle:f.c,VDialog:m.a,VSpacer:x.a})},469:function(t,e,r){var content=r(500);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,r(8).default)("5704c7f8",content,!0,{sourceMap:!1})},499:function(t,e,r){"use strict";r(469)},500:function(t,e,r){(e=r(7)(!1)).push([t.i,"@import url(https://fonts.googleapis.com/css2?family=Kanit:wght@200&display=swap);"]),e.push([t.i,'*{list-style:none;outline:none;font-family:"Kanit",sans-serif;box-sizing:border-box}.fav-container{margin:5px auto;width:90%;position:relative}.sheet-fav-menu{border-radius:10px 10px 0 0;width:100%;padding:20px}.icon-in-add-fav{top:40%}.icon-in-add-fav,.text-in-add-fav{position:absolute;text-align:center;width:100%;left:50%;right:50%;transform:translate(-50%,-50%)}.text-in-add-fav{top:50%;font-weight:700;margin:20px auto}.footer-in-add-fav{position:absolute;text-align:center;width:100%;left:50%;right:50%;transform:translate(-50%,-50%);bottom:0;font-weight:700;margin:20px auto}.footer-in-add-fav a{color:#000;text-decoration:none;transition:.25s ease-in-out}.footer-in-add-fav a:hover{font-size:20px}.menu-card-cober-each-card .menu-card-each-card{padding:15px}.menu-card-each-card .btn-fav-recipe .btn-fav-recipe-icon{position:absolute;left:80%;bottom:43%;background:red;color:#fff;font-size:1.2em;font-weight:700;padding:15px;border-radius:50%;transition:.3s ease-in-out}.menu-card-each-card .btn-fav-recipe .btn-fav-recipe-icon:hover{background:red;color:#fff;transform:scale(1.1)}.header-menu-card-box{background-color:#fff;height:150px;margin-top:50px;padding:20px;border-radius:10px 10px 0 0;width:30%}.header-menu-card-box .header-text{margin:30px auto;background-color:#fff;text-align:center}#card-add-recipe{width:300px}#card-recipe{transition:.25s ease;overflow:hidden}#card-recipe:hover{transform:scale(1.05);box-shadow:5px 5px 15px rgba(0,0,0,.6)}#card-recipe .card-recipe-img{transition:.25s ease}#card-recipe .card-recipe-img:hover .card-recipe-img{transform:scale(1.2)}#card-recipe .menu-card-box-fav{background-color:#fff;margin-left:20px;margin-right:20px;padding:20px}.menu-card-box-fav{background-color:#fff;padding:20px;border-radius:0 0 10px 10px}.card-data .box-card-data{display:flex;justify-content:flex-start;margin:10px auto}@media only screen and (max-width:600px){.sheet-fav-menu{width:100%}#card-add-recipe{height:300px}}@media only screen and (max-width:1264px){.sheet-fav-menu{width:100%}#card-add-recipe{width:258.52px}}@media only screen and (max-width:768px){#card-add-recipe{width:300px}}',""]),t.exports=e},529:function(t,e,r){"use strict";r.r(e);r(53);var n=r(11),o=r(462),c=r(60),d=r.n(c),l={middleware:"authenticated",name:"Favorite",components:{popup:o.a},data:function(){return{absolute:!0,overlay:!1,dialog:!1,dialogSuc:!0,favorite:[],tags:[{tagName:"Drink"},{tagName:"Main Disc"},{tagName:"Burger"},{tagName:"Noodle"},{tagName:"Fruit"},{tagName:"Cheese"},{tagName:"Cream"},{tagName:"Soft Drink"},{tagName:"Steak"},{tagName:"Milk"},{tagName:"Ice cream"}],breadcrumbs:[{text:"หน้าแรก",disabled:!1,href:"/"},{text:"เมนูโปรด",disabled:!0,href:"favorite"}]}},methods:{getFavoriteRecipe:function(){var t=this;return Object(n.a)(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return console.log("geting recipe ..."),t.$store.commit("SET_DIALOG_LOADING",!0),e.next=4,d.a.get("http://127.0.0.1:5000/api/favorite/"+t.$store.getters.getUserID).then((function(e){t.favorite=e.data,console.log("data here",t.favorite)}));case 4:console.log("finished ..."),t.$store.commit("SET_DIALOG_LOADING",!1);case 6:case"end":return e.stop()}}),e)})))()},ClickRecipe:function(t){console.log(t),this.$router.push({path:"recipe",query:{rid:t}})},delFavoriteRecipe:function(t,e){var r=this;return Object(n.a)(regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return r.dialog=!1,console.log("deleteing ..."),r.$store.commit("SET_DIALOG_LOADING",!0),n.next=5,d.a.delete("http://127.0.0.1:5000/api/favorite/"+t+"/"+e).then((function(t){console.log(t)}));case 5:console.log("finished ..."),r.$store.commit("SET_DIALOG_LOADING",!1);case 7:case"end":return n.stop()}}),n)})))()},AddDialog:function(){this.dialog=!0}},mounted:function(){var t=this;return Object(n.a)(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,t.getFavoriteRecipe();case 2:case"end":return e.stop()}}),e)})))()}},v=(r(499),r(29)),f=r(30),m=r.n(f),x=r(463),h=r(441),_=r(425),w=r(411),C=r(263),y=r(477),k=r(460),S=r(172),V=r(262),D=r(461),N=r(413),A=r(448),O=r(455),R=r(39),I=r(496),G=r(481),component=Object(v.a)(l,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"fav-container"},[r("v-dialog",{attrs:{"max-width":"600"},model:{value:t.dialogSuc,callback:function(e){t.dialogSuc=e},expression:"dialogSuc"}},[r("v-card",{attrs:{height:"200"}},[r("v-card-title",{staticClass:"title"},[r("span",{staticStyle:{margin:"10px auto","font-size":"28px","font-weight":"bold"}},[t._v("ลบออกจากเมนูโปรดเรียบร้อย")])]),t._v(" "),r("v-card-actions",[r("v-spacer"),t._v(" "),r("v-btn",{attrs:{color:"green darken-1",text:""},on:{click:function(e){t.dialog=!1}}},[t._v("\n          Agree\n        ")])],1)],1)],1),t._v(" "),r("v-row",{staticClass:"md-6",attrs:{"no-gutters":""}},[r("v-sheet",{staticClass:"sheet-fav-menu",attrs:{color:"white",height:"150"}},[r("v-breadcrumbs",{staticStyle:{position:"absolute",left:"0px",top:"0px"},attrs:{items:t.breadcrumbs,large:""},scopedSlots:t._u([{key:"item",fn:function(e){var n=e.item;return[r("v-breadcrumbs-item",{attrs:{href:n.href,disabled:n.disabled}},[t._v("\n            "+t._s(n.text.toUpperCase())+"\n          ")])]}}])}),t._v(" "),r("h1",{staticStyle:{"text-align":"center","margin-top":"60px"}},[t._v("เมนูโปรด")]),t._v(" "),r("v-btn",{staticStyle:{right:"20px",top:"15px"},attrs:{color:"success",absolute:"",outlined:"",text:""},on:{click:function(e){t.overlay=!t.overlay}}},[r("span",[t._v("แก้ไข")])])],1)],1),t._v(" "),r("div",{staticClass:"menu-card-box-fav"},[r("v-layout",{staticClass:"menu-card-cober-each-card",attrs:{row:"",wrap:""}},[r("v-card",{staticClass:"mx-auto",staticStyle:{margin:"15px 15px",padding:"30px 30px",position:"relative"},attrs:{"max-width":"400",id:"card-add-recipe",height:"400"}},[r("v-btn",{staticClass:"icon-in-add-fav",attrs:{"x-large":"",elevation:"5",icon:"",raised:"",href:"/search"}},[r("v-icon",[t._v("add")])],1),t._v(" "),r("v-card-title",[r("span",{staticClass:"text-in-add-fav"},[t._v("ค้นหาสูตรที่ใช่")])]),t._v(" "),r("span",{staticClass:"footer-in-add-fav"},[r("h5",[t._v("----- หรือ -----")]),t._v(" "),r("a",{attrs:{href:"/add"}},[t._v("เพื่มสูตรของคุณเอง!")])])],1),t._v(" "),r("v-sheet",{staticClass:"pa-3",attrs:{color:"grey lighten-4"}},[r("v-skeleton-loader",{staticClass:"mx-auto",attrs:{"max-width":"300",width:"400",type:"card"}})],1),t._v(" "),t._l(t.favorite,(function(e){return r("v-flex",{key:e.fav_id,staticClass:"menu-card-each-card",attrs:{xs12:"",sm6:"",md4:"",lg3:""}},[r("div",{staticClass:"dialog_popup"},[r("v-dialog",{staticClass:"popup-submit-delete",attrs:{width:"600px"},model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[r("v-card",{staticClass:"card-popup",attrs:{width:"100%"}},[r("div",{staticStyle:{"text-align":"center",padding:"20px"}},[r("span",{staticStyle:{"font-size":"24px","font-weight":"bold"}},[t._v("จะลบสูตรนี้ออกจากเมนูโปรดหรือไม่?")])]),t._v(" "),r("div",{staticClass:"div-action",staticStyle:{display:"block",width:"60%",margin:"0px auto",padding:"20px"}},[r("v-btn",{staticClass:"submit",attrs:{color:"success"},on:{click:function(r){return t.delFavoriteRecipe(e.fav_id,e.recipe_id)}}},[t._v("ยืนยัน")]),t._v(" "),r("v-btn",{staticClass:"cancel",attrs:{color:"warning"}},[t._v("ยกเลิก")])],1)])],1)],1),t._v(" "),r("v-card",{staticClass:"mx-auto",attrs:{loading:t.loading,"max-width":"400",id:"card-recipe"}},[r("div",{staticClass:"card-recipe-zoom",staticStyle:{overflow:"hidden"}},[r("v-img",{staticClass:"card-recipe-img",attrs:{height:"200",src:e.photo_recipe}})],1),t._v(" "),r("div",{staticClass:"btn-fav-recipe"},[r("div",[r("v-icon",{staticClass:"btn-fav-recipe-icon"},[t._v("favorite_border")])],1)]),t._v(" "),r("v-card-title",{staticStyle:{"font-size":"28px"}},[t._v(t._s(e.title))]),t._v(" "),r("v-card-text",{staticClass:"card-data"},[r("div",{staticClass:"box-card-data"},[r("div",{staticClass:"card-data-cook-time"},[r("v-icon",{attrs:{left:""}},[t._v("schedule")]),t._v(" "),r("span",{staticStyle:{"vertical-align":"middle"}},[t._v(t._s(e.serve)+" ชั่วโมง")])],1),t._v(" "),r("div",{staticClass:"card-data-cook-time",staticStyle:{"margin-left":"15px"}},[r("v-icon",{attrs:{left:""}},[t._v("group")]),t._v(" "),r("span",{staticStyle:{"vertical-align":"middle"}},[t._v("สำหรับ 2 ที่")])],1)]),t._v(" "),r("v-row",{staticClass:"mx-0",attrs:{align:"center"}},[r("v-rating",{attrs:{value:"4.5",color:"amber",dense:"","half-increments":"",readonly:"",size:"14"}}),t._v(" "),r("div",{staticClass:"grey--text ml-4"},[t._v(t._s(e.serve)+" (413)")])],1)],1),t._v(" "),r("v-card-actions",[r("v-btn",{staticStyle:{"background-color":"#ff7043"},attrs:{block:"",dark:"",text:""},on:{click:function(r){return t.ClickRecipe(e.recipe_id)}}},[r("span",[t._v("ทำอาหาร")])])],1),t._v(" "),r("v-overlay",{attrs:{absolute:t.absolute,value:t.overlay}},[r("v-btn",{attrs:{color:"warning"},on:{click:function(e){t.overlay=!1}}},[r("span",{on:{click:t.AddDialog}},[t._v("ลบออกจากเมนูโปรด")])])],1)],1)],1)}))],2)],1)],1)}),[],!1,null,null,null);e.default=component.exports;m()(component,{VBreadcrumbs:x.a,VBreadcrumbsItem:h.a,VBtn:_.a,VCard:w.a,VCardActions:C.a,VCardText:C.b,VCardTitle:C.c,VDialog:y.a,VFlex:k.a,VIcon:S.a,VImg:V.a,VLayout:D.a,VOverlay:N.a,VRating:A.a,VRow:O.a,VSheet:R.a,VSkeletonLoader:I.a,VSpacer:G.a})}}]);