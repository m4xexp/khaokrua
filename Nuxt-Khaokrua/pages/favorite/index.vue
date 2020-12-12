<template>
  <div class="fav-container">

    <v-dialog v-model="dialogSuc" max-width="600">
      <v-card height="200">
        <v-card-title class="title">
          <span style="margin: 10px auto; font-size: 28px; font-weight: bold"
            >ลบออกจากเมนูโปรดเรียบร้อย</span
          >
        </v-card-title>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="green darken-1" text @click="dialog = false">
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

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

        <h1 style="text-align: center; margin-top: 60px">เมนูโปรด</h1>

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

    <div class="menu-card-box-fav">
      <v-layout row wrap class="menu-card-cober-each-card">
        <v-card
          class="mx-auto"
          max-width="400"
          style="margin: 15px 15px; padding: 30px 30px; position: relative"
          id="card-add-recipe"
          height="400"
        >
          <v-btn
            x-large
            elevation="5"
            icon
            raised
            class="icon-in-add-fav"
            href="/search"
          >
            <v-icon>add</v-icon>
          </v-btn>
          <v-card-title
            ><span class="text-in-add-fav">ค้นหาสูตรที่ใช่</span>
          </v-card-title>

          <span class="footer-in-add-fav">
            <h5>----- หรือ -----</h5>
            <a href="/add">เพื่มสูตรของคุณเอง!</a>
          </span>
        </v-card>

        <!-- <v-sheet
          :color="`grey lighten-4`"
          class="pa-3"
        >
          <v-skeleton-loader
            class="mx-auto"
            max-width="300"
            width="400"
            type="card"
          ></v-skeleton-loader>
        </v-sheet> -->

        <!-- Main favorite card -->

        <v-flex
          xs12
          sm6
          md4
          lg3
          v-for="fav in favorite"
          :key="fav.fav_id"
          class="menu-card-each-card"
        >
          <div class="dialog_popup">
            <v-dialog
              v-model="dialog"
              class="popup-submit-delete"
              width="600px"
            >
              <v-card class="card-popup" width="100%">
                <div style="text-align: center; padding: 20px">
                  <span style="font-size: 24px; font-weight: bold"
                    >จะลบสูตรนี้ออกจากเมนูโปรดหรือไม่?</span
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
                    @click="delFavoriteRecipe(fav.fav_id, fav.recipe_id)"
                    color="success"
                    class="submit"
                    >ยืนยัน</v-btn
                  >
                  <v-btn color="warning" class="cancel">ยกเลิก</v-btn>
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
            <!-- Img for recipe card -->

            <div class="card-recipe-zoom" style="overflow: hidden">
              <v-img
                class="card-recipe-img"
                height="200"
                :src="fav.photo_recipe"
              ></v-img>
            </div>

            <div class="btn-fav-recipe">
              <div>
                <v-icon class="btn-fav-recipe-icon">favorite_border</v-icon>
              </div>
            </div>

            <v-card-title style="font-size: 28px">{{ fav.title }}</v-card-title>

            <v-card-text class="card-data">
              <div class="box-card-data">
                <div class="card-data-cook-time">
                  <v-icon left>schedule</v-icon>
                  <span style="vertical-align: middle"
                    >{{ fav.serve }} ชั่วโมง</span
                  >
                </div>
                <div class="card-data-cook-time" style="margin-left: 15px">
                  <v-icon left>group</v-icon>
                  <span style="vertical-align: middle">สำหรับ 2 ที่</span>
                </div>
              </div>

              <v-row align="center" class="mx-0">
                <v-rating
                  value="4.5"
                  color="amber"
                  dense
                  half-increments
                  readonly
                  size="14"
                ></v-rating>

                <div class="grey--text ml-4">{{ fav.serve }} (413)</div>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-btn
                block
                dark
                text
                @click="ClickRecipe(fav.recipe_id)"
                style="background-color: #ff7043"
              >
                <span>ทำอาหาร</span>
              </v-btn>
            </v-card-actions>

            <v-overlay :absolute="absolute" :value="overlay">
              <v-btn color="warning" @click="overlay = false">
                <span @click="AddDialog">ลบออกจากเมนูโปรด</span>
              </v-btn>
            </v-overlay>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
    <v-dialog persistent v-model="success_fav" width="500">
      <v-card>
        <v-card-title color="#00E676"> แจ้งเตือน </v-card-title>
        <v-card-text class="textDetail">
          ลบออกจากเมนูโปรดเรียบร้อย
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="success_fav = !success_fav "
          >
            ตกลง
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>

import popup from '~/components/Popup/popup.vue'
import axios from 'axios'

export default {
  // middleware: 'authenticated',

  name: 'Favorite',

  components: { popup },

  data: () => ({
    success_fav: false,
    absolute: true,
    overlay: false,
    dialog: false,
    dialogSuc: false,
    favorite: [],
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
        text: 'เมนูโปรด',
        disabled: true,
        href: 'favorite',
      },
    ],
  }),
  methods: {
    async getFavoriteRecipe() {
      console.log('geting recipe ...')
      this.$store.commit('SET_DIALOG_LOADING', true)
      await axios
        .get(
          'http://127.0.0.1:5000/api/favorite/' + this.$store.getters.getUserID
        )
        .then((res) => {
          this.favorite = res.data
          console.log('data here', this.favorite)
        })
      console.log('finished ...')
      this.$store.commit('SET_DIALOG_LOADING', false)
    },

    ClickRecipe(id) {
      console.log(id)
      this.$router.push({ path: 'recipe', query: { rid: id } })
    },

    async delFavoriteRecipe(fav_id, recipe_id) {
      this.dialog = false
      console.log('deleteing ...')
      this.$store.commit('SET_DIALOG_LOADING', true)
      await axios
        .delete(
          'http://127.0.0.1:5000/api/favorite/' + fav_id + '/' + recipe_id
        )
        .then((res) => {
          console.log(res)
        })
      console.log('finished ...')
      this.$store.commit('SET_DIALOG_LOADING', false)
      this.success_fav = true
    
    },

    AddDialog() {
      this.dialog = true
    },
  },
  async mounted() {
    await this.getFavoriteRecipe()
  },
}
</script>

<style lang="scss">
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

#card-recipe .menu-card-box-fav {
  background-color: white;
  margin-left: 20px;
  margin-right: 20px;
  padding: 20px;
}

.menu-card-box-fav {
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


