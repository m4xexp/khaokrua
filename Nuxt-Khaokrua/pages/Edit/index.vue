<template>
  <div class="add-container">
    <v-row id="row-first" no-gutters class="md-6" justify="center">
      <v-sheet color="white" height="150" class="header-sheet-add-menu">
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
        <h1 style="text-align: center; margin-top: 60px">แก้ไขสูตรอาหาร</h1>
      </v-sheet>
    </v-row>

    <v-row id="row-second" no-gutters class="md-6">
      <v-sheet class="sheet-add-menu">
        <!-- For menu title and Description -->

        <div class="wraper-sheet-add-menu">
          <div class="field-recipe-title">
            <div style="display: flex">
              <v-text-field
                outlined
                label="ชื่อเมนู"
                append-icon="help_outline"
                v-model="DataRecipe.title"
              >
              </v-text-field>
            </div>

            <v-textarea
              outlined
              label="รายละเอียด"
              v-model="DataRecipe.description"
            ></v-textarea>
          </div>

          <!-- For categlory -->

          <div class="field-recipe-categlories" style="height: 200px">
            <span class="categlory-header">หมวดหมู่</span>
            <v-divider style="margin: 5px 0px 20px 0px"></v-divider>
            <div class="auto-tag-field">
              <v-autocomplete
                v-model="DataRecipe.recipe_tag"
                chips
                deletable-chips
                outlined
                :items="states"
                label="ทำไรกินดีน้า"
              >
              </v-autocomplete>
              <v-btn icon class="icon-more-tag-categlory"
                ><v-icon>more_horiz</v-icon></v-btn
              >
            </div>
          </div>

          <!-- For recipe data like prep time -->

          <div class="field-recipe-detail">
            <div class="div-card-add-recipe-img">
              <v-card
                class="mx-auto"
                max-width="400"
                id="card-add-recipe-img"
                height="200px"
                width="240px"
              >
                <v-btn
                  x-large
                  elevation="5"
                  icon
                  raised
                  class="icon-in-add-img"
                  @click="openUploadModal"
                >
                  <v-icon>add</v-icon>
                </v-btn>
                <v-card-title
                  ><span class="text-in-add-img">เพิ่มรูปภาพ</span>
                </v-card-title>
              </v-card>
            </div>

            <div class="all-data" style="display: block">
              <div class="recipe-data">
                <span>เวลาเตรียม :</span>
                <div class="prep-time">
                  <div class="prep-time-input">
                    <v-text-field
                      solo
                      placeholder="เวลาเตรียม"
                      v-model="prep_time.num"
                    >
                    </v-text-field>
                  </div>
                  <div class="prep-time-select">
                    <v-select
                      :items="prep"
                      label="เวลา"
                      solo
                      v-model="prep_time.unit"
                    ></v-select>
                  </div>
                </div>
              </div>
              <div class="recipe-data">
                <span>เวลาทำอาหาร :</span>
                <div class="cook-time">
                  <div class="cook-time-input">
                    <v-text-field
                      solo
                      placeholder="เวลาปรุง"
                      v-model="DataRecipe.cook_time"
                    >
                    </v-text-field>
                  </div>
                  <div class="cook-time-select">
                    <v-select
                      :items="cookTime"
                      label="เวลา"
                      solo
                      v-model="cook_time.unit"
                    ></v-select>
                  </div>
                </div>
              </div>

              <v-divider class="divider-between-prep"></v-divider>

              <div class="recipe-data">
                <span>เสิร์ฟ :</span>
                <div class="for-serve">
                  <div class="serve-input">
                    <v-text-field
                      solo
                      placeholder="สำหรับกี่ที่"
                      v-model="DataRecipe.serve"
                    >
                    </v-text-field>
                  </div>
                </div>
              </div>
              <div class="recipe-data" style="display: block">
                <span>จำนวน :</span>
                <div class="for-yield">
                  <div class="yield-input">
                    <v-text-field solo placeholder="จำนวน" v-model="DataRecipe.yield">
                    </v-text-field>
                  </div>
                  <div class="yield-select">
                    <v-text-field solo v-model="yield2.unit"> </v-text-field>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ingredients text area -->

          <div class="field-recipe-directions">
            <span class="directions-header">ส่วนผสม</span>
            <v-divider style="margin: 5px 0px 20px 0px"></v-divider>

            <div style="display: flex; justify-content: space-between">
              <v-textarea
                v-model="DataRecipe.ingredients"
                outlined
                clearable
                placeholder="เช่น ไข่ไก่ 3 ฟอง"
                style="margin-top: 25px"
              ></v-textarea>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="#757575" dark v-bind="attrs" v-on="on">
                    help_outline
                  </v-icon>
                </template>
                <span
                  >ใส่ส่วนผสม 1 อย่างต่อ 1 แถว และใส่หน่วยของส่วนผสมต่อท้าย เช่น
                  น้ำปลา 1 ช้อนโต๊ะ</span
                >
              </v-tooltip>
            </div>
          </div>

          <!-- directions text area -->

          <div class="field-recipe-directions">
            <span class="directions-header">วิธีทำ</span>
            <v-divider style="margin: 5px 0px 20px 0px"></v-divider>

            <div style="display: flex; justify-content: space-between">
              <v-textarea
                v-model="DataRecipe.steps"
                outlined
                clearable
                placeholder="เช่น ตั้งกระทะใส่น้ำมันเยอะๆ เปิดไฟกลางแล้วรอให้น้ำมันร้อนจัด"
                style="margin-top: 25px"
              ></v-textarea>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="#757575" dark v-bind="attrs" v-on="on">
                    help_outline
                  </v-icon>
                </template>
                <span
                  >ใส่เลขลำดับวิธีทำไว้ด้านหน้า
                  และเมื่อเขียนวิธีทำครบในแต่ละขั้นตอนแล้ว ควรเว้นบรรทัด 1
                  บรรทัด</span
                >
              </v-tooltip>
            </div>
          </div>

          <div class="btn-for-add-recipe">
            <div class="btn-save">
              <v-btn x-large color="success" @click="saveRecipeData"
                ><span>บันทึก</span></v-btn
              >
            </div>
            <div class="btn-cancel">
              <span>หรือ</span>
              <a href="#" style="text-decoration: none">ยกเลิก</a>
            </div>
          </div>
        </div>
      </v-sheet>

      <!-- Stepper -->
    </v-row>
    <v-dialog persistent v-model="success" width="500">
      <v-card>
        <v-card-title color="#00E676"> แจ้งเตือน </v-card-title>
        <v-card-text class="textDetail">
          แก้ไขสูตรอาหารเรียบร้อย
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="success = !success"
          >
            ตกลง
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios'
import recipe from '../../services/recipe'
import popup from '../../components/Popup/popup'
import success from '../../components/Popup/Success'
import Success from '../../components/Popup/Success.vue'

export default {
  name: 'edit',
  components: {Success},

  data: () => ({
    success: false,
    states: [],
    prep: ['นาที', 'ชั่วโมง', 'วัน'],
    cookTime: ['นาที', 'ชั่วโมง', 'วัน'],

    breadcrumbs: [
      {
        text: 'หน้าแรก',
        disabled: false,
        href: '/',
      },
      {
        text: 'แก้ไขสูตรอาหาร',
        disabled: true,
        href: 'add',
      },
    ],

    prep_time: {
      num: '',
      unit: '',
    },
    cook_time: {
      num: '',
      unit: '',
    },
    serve: '',
    yield2: {
      num: '',
      unit: '',
    },

    DataRecipe: {
      author: '',
      cook_time: '',
      description: '',
      ingredients: '',

      photo_recipe:
        'https://img.freepik.com/free-photo/board-amidst-cooking-ingredients_23-2147749529.jpg',
      prep_time: '',
      profile_name: '',
      recipe_id: '',
      serve: '',
      steps: '',
      title: null,
      yield: '',
      recipe_tag: '',
    },
    nextRid: '',

  }),
  async mounted() {
    this.$store.commit('SET_DIALOG_LOADING', true)
    var rid = this.$route.query.rid
    this.nextRid = this.rid
    var result = await axios
      .get('http://127.0.0.1:5000/api/recipe/' + rid)
      .then((res) => {
        console.log('Here',res.data[0])
        this.DataRecipe = res.data[0]
        this.DataRecipe.title = res.data[0].title
        this.DataRecipe.author = res.data[0].author
        this.DataRecipe.cook_time = res.data[0].cook_time
        this.DataRecipe.description = res.data[0].description
        this.DataRecipe.ingredients = res.data[0].ingredients
        this.DataRecipe.photo_recipe = res.data[0].author
        this.DataRecipe.prep_time = res.data[0].cook_time
        this.DataRecipe.yield = res.data[0].yield
        this.DataRecipe.steps = res.data[0].steps
        this.DataRecipe.serve = res.data[0].serve
      })
    this.$store.commit('SET_DIALOG_LOADING', false)
    
  },
  methods: {
    openUploadModal() {
      window.cloudinary
        .openUploadWidget(
          {
            cloud_name: 'khaokruacooking',
            upload_preset: 'imgkhaokruacook',
          },
          (error, result) => {
            if (!error && result && result.event === 'success') {
              console.log('Done uploading..: ', result.info)
              console.log('here is your pic!', result.info.url)
              this.DataRecipe.photo_recipe = result.info.url
              console.log('your finally pic!', this.DataRecipe.photo_recipe)
            }
          }
        )
        .open()
    },
    async saveRecipeData(event) {
      var rid = this.$route.query.rid
      this.$store.commit('SET_DIALOG_LOADING', true)
      event.preventDefault()
      this.DataRecipe.serve = this.serve
      this.DataRecipe.prep_time = this.prep_time.num + ' ' + this.prep_time.unit
      this.DataRecipe.cook_time = this.cook_time.num + ' ' + this.cook_time.unit
      this.DataRecipe.yield = this.yield2.num + ' ' + this.yield2.unit
      console.warn(this.DataRecipe)
      console.warn('Before in to bodyform', this.$store.getters.getUserID)
      var bodyFormData = new FormData()
      bodyFormData.append('recipe_id', this.DataRecipe.recipe_id)
      bodyFormData.append('title', this.DataRecipe.title)
      bodyFormData.append('description', this.DataRecipe.description)
      bodyFormData.append('photo_recipe', this.DataRecipe.photo_recipe)
      bodyFormData.append('serve', this.DataRecipe.serve)
      bodyFormData.append('prep_time', this.DataRecipe.prep_time)
      bodyFormData.append('cook_time', this.DataRecipe.cook_time)
      bodyFormData.append('yield2', this.DataRecipe.yield)
      bodyFormData.append('ingredients', this.DataRecipe.ingredients)
      bodyFormData.append('steps', this.DataRecipe.steps)
      bodyFormData.append('tag', this.DataRecipe.recipe_tag)
      bodyFormData.append('author', this.$store.getters.getUserID)

      await axios({
        method: 'put',
        url: 'http://127.0.0.1:5000/api/recipe/edit ',
        data: bodyFormData,
        headers: { 'Content-Type': 'multipart/form-data' },
      })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })

      console.log('Body Form', this.DataRecipe)
      this.$store.commit('SET_DIALOG_LOADING', false)
      this.success = true
    },
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

#row-header {
  width: 97%;
  margin-left: 20px;
  display: flex;
}

#row-container {
  width: 97%;
  margin-left: 20px;
  display: flex;
}

.add-container {
  margin: 15px auto;
  width: 90%;
  position: relative;
}

.wraper-sheet-add-menu {
  width: 90%;
}

.header-sheet-add-menu {
  border-radius: 10px 10px 0px 0px;
  width: 100%;
  padding: 20px;
}

.sheet-add-menu {
  border-radius: 0px 0px 0px 0px;
  width: 100%;
  padding: 20px;
}

.auto-tag-field {
  height: 70px;
  display: flex;
  position: relative;
}

.categlory-header {
  font-size: 45px;
  margin: 20px auto;
}

.icon-more-tag-categlory {
  margin-top: 15px;
}

.field-recipe-detail {
  display: flex;
  justify-content: space-around;
}

.field-recipe-detail .all-data {
  width: 50%;
}

.recipe-data {
  display: block;
}

.recipe-data .prep-time {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.prep-time .prep-time-input {
  width: 20%;
  margin-left: 20px;
}

.prep-time-select {
  width: 65%;
  margin-right: 40px;
}

.recipe-data .cook-time {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.cook-time .cook-time-input {
  width: 20%;
  margin-left: 20px;
}

.cook-time-select {
  width: 65%;
  margin-right: 40px;
}

.recipe-data .for-serve {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.serve-input {
  width: 20%;
  margin-left: 20px;
}

.recipe-data .for-yield {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.yield-input {
  width: 20%;
  margin-left: 20px;
}

.yield-select {
  width: 65%;
  margin-right: 40px;
}

.divider-between-prep {
  margin: 10px auto;
  margin-bottom: 25px;
  width: 90%;
}

.div-card-add-recipe-img {
  margin-left: 40px;
}

#card-add-recipe-img {
  margin-top: 15px;
  padding: 30px 30px;
  position: relative;
}

.icon-in-add-img {
  position: absolute;
  text-align: center;
  width: 100%;
  left: 50%;
  right: 50%;
  transform: translate(-50%, -50%);
  top: 40%;
}

.text-in-add-img {
  position: absolute;
  text-align: center;
  width: 100%;
  left: 50%;
  right: 50%;
  transform: translate(-50%, -50%);
  top: 50%;
  font-weight: bold;
  margin: 30px auto;
}

.ingredients-header {
  font-size: 45px;
  margin: 20px auto;
}

.field-recipe-ingredients {
  display: block;
}

.btn-for-add-recipe {
  width: 100%;
  display: flex;
  justify-content: center;
}

.text-label {
  display: flex;
}

.input-name {
  width: 60%;
}

.btn-cancel {
  padding: 15px;
}

.ingredient-item-label {
  font-size: 16px;
}

.delete-ingredient {
  cursor: pointer;
  transition: 0.25s ease-in-out;
  margin-top: 28px;
  margin-left: 10px;
  &:hover {
    transform: scale(1.2);
  }
}

.ingredient-item-edit {
  width: 100%;
  margin-top: 15px;
}

.directions-header {
  font-size: 45px;
  margin: 20px auto;
}

.directions-item-label {
  font-size: 16px;
}

.delete-directions {
  cursor: pointer;
  transition: 0.25s ease-in-out;
  &:hover {
    transform: scale(1.2);
  }
}

.directions-item-edit {
  width: 100%;
  margin-top: 15px;
}

.ActionAddIngred {
  display: flex;
}

.ingredients-field {
  display: flex;
  position: relative;
  height: 70px;
  justify-content: space-between;
}

@media only screen and (max-width: 960px) {
  #card-add-recipe-img {
    width: 200px;
  }
  .div-card-add-recipe-img {
    margin-left: 20px;
  }
  .yield-select {
    margin-right: 20px;
  }
  .serve-select {
    margin-right: 20px;
  }
  .cook-time-select {
    margin-right: 20px;
  }
  .prep-time-select {
    margin-right: 20px;
  }
}

@media only screen and (max-width: 1264px) {
  #card-add-recipe-img {
    width: 200px;
  }
  .div-card-add-recipe-img {
    margin-left: 20px;
  }
  .yield-select {
    margin-right: 20px;
  }
  .serve-select {
    margin-right: 20px;
  }
  .cook-time-select {
    margin-right: 20px;
  }
  .prep-time-select {
    margin-right: 20px;
  }
}

@media only screen and (max-width: 600px) {
  #card-add-recipe-img {
    width: 200px;
  }
  .wraper-sheet-add-menu {
    width: 100%;
  }

  .div-card-add-recipe-img {
    margin: 25px auto;
  }
  .yield-select {
    margin-right: 20px;
  }
  .serve-select {
    margin-right: 20px;
  }
  .cook-time-select {
    margin-right: 20px;
  }
  .prep-time-select {
    margin-right: 20px;
  }
  .field-recipe-detail .all-data {
    width: 100%;
  }

  .field-recipe-detail {
    display: block;
  }
}
</style>