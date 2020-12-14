<template>
  <div class="fav-container">
    <div class="wrapper-fav">
      <v-row no-gutters class="md-6">
        <v-sheet color="white" height="150" class="sheet-fav-menu">
          <v-breadcrumbs
            :items="breadcrumbs"
            style="position: absolute; left: 0px; top: 0px"
            large
          >
            <template v-slot:item="{ item }">
              <v-breadcrumbs-item :href="item.href" :disabled="item.disabled">
                {{ item.text.toUpperCase() }}
              </v-breadcrumbs-item>
            </template>
          </v-breadcrumbs>

          <h1 style="text-align: center; margin-top: 60px">สูตรของฉัน</h1>

          <v-btn
            color="success"
            absolute
            outlined
            text
            style="right: 20px; top: 15px"
            @click="overlay = !overlay"
            ><span>แก้ไข</span></v-btn
          >
        </v-sheet>
      </v-row>

      <!-- Card menu -->

      <div class="menu-card-box-my">
        <v-layout row wrap class="menu-card-cober-each-card">
          <!-- Main favorite card -->

          <v-flex
            xs12
            sm6
            md4
            lg3
            v-for="my in myData"
            :key="my.recipe_id"
            class="menu-card-each-card"
          >
            <div class="dialog_popup_del">
              <v-dialog
                v-model="dialogDel"
                class="popup-submit-delete"
                width="600px"
              >
                <v-card class="card-popup" width="100%">
                  <div style="text-align: center; padding: 20px">
                    <span style="font-size: 24px; font-weight: bold"
                      >จะลบสูตรนี้ออกหรือไม่?</span
                    >
                  </div>

                  <div
                    class="div-action"
                    style="
                      display: block;
                      width: 60%;
                      margin: 0px auto;
                      padding: 20px;
                    "
                  >
                    <v-btn
                      @click="delMyRecipe(my.recipe_id)"
                      color="success"
                      class="submit"
                      >ยืนยัน</v-btn
                    >
                    <v-btn color="warning" @click="DisDialog" class="cancel"
                      >ยกเลิก</v-btn
                    >
                  </div>
                </v-card>
              </v-dialog>
            </div>

            <!-- Card -->

            <v-card
              :loading="loading"
              class="mx-auto"
              max-width="400"
              id="card-recipe"
            >
              <template slot="progress">
                <v-progress-linear
                  color="deep-purple"
                  height="10"
                  indeterminate
                ></v-progress-linear>
              </template>

              <!-- Img for recipe card -->

              <div class="card-recipe-zoom" style="overflow: hidden">
                <v-img
                  class="card-recipe-img"
                  height="200"
                  :src="my.photo_recipe"
                ></v-img>
              </div>

              <div class="btn-fav-recipe">
                <div>
                  <v-icon class="btn-fav-recipe-icon" style=""
                    >favorite_border</v-icon
                  >
                </div>
              </div>

              <v-card-title style="font-size: 28px">{{
                my.title
              }}</v-card-title>

              <v-card-text class="card-data">
                <div class="box-card-data">
                  <div class="card-data-cook-time">
                    <v-icon left>schedule</v-icon>
                    <span style="vertical-align: middle"
                      >{{ my.serve }} ชั่วโมง</span
                    >
                  </div>
                  <div class="card-data-cook-time" style="margin-left: 15px">
                    <v-icon left>group</v-icon>
                    <span style="vertical-align: middle">สำหรับ 2 ที่</span>
                  </div>
                </div>

                <v-row align="center" class="mx-0">
                  <v-rating
                    :value="4"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="14"
                  ></v-rating>

                  <div class="grey--text ml-4">4 (413)</div>
                </v-row>
              </v-card-text>

              <v-card-actions>
                <v-btn
                  block
                  dark
                  text
                  @click="clicktoRecipe(my.recipe_id)"
                  style="background-color: #ff7043"
                >
                  <span>ทำอาหาร</span>
                </v-btn>
              </v-card-actions>

              <v-overlay :absolute="absolute" :value="overlay">
                <v-btn color="warning" @click="overlay = false" class="editBtn">
                  <span @click="ClickEditRecipe(my.recipe_id)">แก้ไขสูตร</span>
                </v-btn>
                <v-btn color="warning">
                  <span @click="dialogDel = !dialogDel" class="delBtn"
                    >ลบสูตร</span
                  >
                </v-btn>
              </v-overlay>
            </v-card>
          </v-flex>
        </v-layout>
      </div>
    </div>
    <v-dialog persistent v-model="del_success" width="500">
      <v-card>
        <v-card-title color="#00E676"> แจ้งเตือน </v-card-title>
        <v-card-text class="textDetail">
          ลบสูตรอาหารเรียบร้อย
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="del_success = !del_success"
          >
            ตกลง
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
// import Pagination from "./Pagination.vue";
// import Searchrecipe from "./SearchRecipe.vue";
import axios from 'axios'

export default {
  name: 'myRecipe',

  components: {},

  pagination() {
    return {
      page: 1,
    }
  },

  data: () => ({
    del_success: false,
    loading: false,
    dialogEdit: false,
    dialogDel: false,
    selection: 1,
    absolute: true,
    overlay: false,
    menus: [
      {
        Name: 'ต้มยำกุ้ง',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src:
          'https://d12man5gwydfvl.cloudfront.net/wp-content/uploads/2019/06/shutterstock_430308484.jpg',
      },
      {
        Name: 'ข้าวผัด',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src:
          'https://i.pinimg.com/originals/8b/52/0c/8b520ccac4a4372d62d33770ece3c529.jpg',
      },
      {
        Name: 'กะเพราทะเล',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src: 'https://f.ptcdn.info/206/064/000/ps7ec58xwloZzLEw1eDJ-o.jpg',
      },
      {
        Name: 'พิซซ่า',
        Author: 'KhaoKrua',
        time: '1',
        rate: 4.7,
        src:
          'https://caffedolcemissoula.com/wp-content/uploads/2019/09/Pizza.jpg',
      },
    ],
    tags: [
      { tagName: 'Drink' },
      { tagName: 'Main Disc' },
      { tagName: 'Burger' },
      { tagName: 'Noodle' },
      { tagName: 'Fruit' },
      { tagName: 'Cheese' },
      { tagName: 'Cream' },
      { tagName: 'Soft Drink' },
      { tagName: 'Steak' },
      { tagName: 'Milk' },
      { tagName: 'Ice cream' },
    ],
    breadcrumbs: [
      {
        text: 'หน้าแรก',
        disabled: false,
        href: '/',
      },
      {
        text: 'สูตรของฉัน',
        disabled: true,
        href: 'favorite',
      },
    ],
    myData: [],
    dialog: false,
  }),
  methods: {
    async getMyRecipe() {
      console.log('geting recipe ...')
      this.$store.commit('SET_DIALOG_LOADING', true)
      await axios
        .get('http://127.0.0.1:5000/api/myrecipe/' + localStorage.getItem('USERNAME'))
        .then((res) => {
          this.myData = res.data
          console.log(res)
        })
      console.log('finished ...')
      this.$store.commit('SET_DIALOG_LOADING', false)
    },

    async delMyRecipe(recipe_id) {
      console.log(recipe_id)
      this.dialogDel = false
      console.log('deleteing ...')
      this.$store.commit('SET_DIALOG_LOADING', true)
      await axios
        .delete('http://127.0.0.1:5000/api/recipe/' + recipe_id)
        .then((res) => {
          console.log(res)
        })
      console.log('finished ...')
      this.$store.commit('SET_DIALOG_LOADING', false)
      this.del_success = true
    },

    ClickEditRecipe(id) {
      console.log(id)
      this.$router.push({ path: 'edit', query: { rid: id } })
    },


    clicktoRecipe(id) {
      console.log('id for delete recipe',id)
      this.$router.push({ path: 'recipe', query: { rid: id } })
    },

    DisDialog() {
      this.dialog = false
    },
  },

  mounted() {
    this.getMyRecipe()
  },
}
</script>


<style lang="scss" >
@import url('https://fonts.googleapis.com/css2?family=Kanit:wght@200&display=swap');

* {
  list-style: none;
  outline: none;
  font-family: 'Kanit', sans-serif;
  box-sizing: border-box;
}

.fav-container {
  margin: 5px auto;
  width: 90%;
  position: relative;
}

.sheet-fav-menu {
  border-radius: 10px 10px 0px 0px;
  padding: 50px;
  margin-top: 0 auto;
  width: 100%;
}

.sheet-fav-menu {
  border-radius: 10px 10px 0px 0px;
  width: 100%;
  padding: 20px;
}

.icon-in-add-fav {
  position: absolute;
  text-align: center;
  width: 100%;
  left: 50%;
  right: 50%;
  transform: translate(-50%, -50%);
  top: 40%;
}

.text-in-add-fav {
  position: absolute;
  text-align: center;
  width: 100%;
  left: 50%;
  right: 50%;
  transform: translate(-50%, -50%);
  top: 50%;
  font-weight: bold;
  margin: 20px auto;
}

.footer-in-add-fav {
  position: absolute;
  text-align: center;
  width: 100%;
  left: 50%;
  right: 50%;
  transform: translate(-50%, -50%);
  bottom: 0;
  font-weight: bold;
  margin: 20px auto;
}

.footer-in-add-fav a {
  color: rgb(0, 0, 0);
  text-decoration: none;
  transition: 0.25s ease-in-out;
  &:hover {
    font-size: 20px;
  }
}

.menu-card-cober-each-card .menu-card-each-card {
  padding: 15px 15px 15px 15px;
}

.menu-card-each-card .btn-fav-recipe .btn-fav-recipe-icon {
  position: absolute;
  left: 80%;
  bottom: 43%;
  background: red;
  color: white;
  font-size: 1.2em;
  font-weight: bold;
  padding: 15px;
  border-radius: 50%;
  transition: 0.3s ease-in-out;
  cursor: pointer;
  &:hover {
    background: red;
    color: white;
    transform: scale(1.1);
  }
}

.menu-card-each-card .btn-fav-recipe .btn-fav-recipe-icon:hover {
  transform: scale(1.1);
}

.header-menu-card-box {
  background-color: white;
  height: 150px;
  margin-top: 50px;
  padding: 20px;
  border-radius: 10px 10px 0px 0px;
  width: 30%;
}

.header-menu-card-box .header-text {
  margin: 30px auto;
  background-color: white;
  text-align: center;
}

#card-add-recipe {
  width: 300px;
}

#card-recipe {
  transition: 0.25s ease;
  overflow: hidden;
  // cursor: pointer;
  &:hover {
    transform: scale(1.05);
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.6);
  }
}

#card-recipe .card-recipe-img {
  transition: 0.25s ease;
  &:hover .card-recipe-img {
    transform: scale(1.2);
  }
}

#card-recipe .menu-card-box-my {
  background-color: white;
  margin-left: 20px;
  margin-right: 20px;
  padding: 20px;
}

.menu-card-box-my {
  background-color: white;
  padding: 20px;
  border-radius: 0px 0px 10px 10px;
}

.card-data .box-card-data {
  display: flex;
  justify-content: flex-start;
  margin: 10px auto;
}

@media only screen and (max-width: 600px) {
  .sheet-fav-menu {
    width: 100%;
  }
  #card-add-recipe {
    height: 300px;
  }
}

@media only screen and (max-width: 1264px) {
  .sheet-fav-menu {
    width: 100%;
  }
  #card-add-recipe {
    width: 258.52px;
  }
}

@media only screen and (max-width: 768px) {
  #card-add-recipe {
    width: 300px;
  }
}
</style>


