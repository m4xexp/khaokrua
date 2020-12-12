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

        <div
          class="wraper-sheet-add-menu"
          v-for="data in recipeDetail"
          :key="data.recipe_id"
        >
          <div class="field-recipe-title">
            <div style="display: flex">
              <v-text-field
                outlined
                label="ชื่อเมนู"
                append-icon="help_outline"
                v-model="recipeDetail.title"
                :value="data.title"
              >
              </v-text-field>
            </div>

            <v-textarea
              outlined
              label="รายละเอียด"
              v-model="data.RecipeCaption"
            ></v-textarea>
          </div>

          <!-- For categlory -->

          <div class="field-recipe-categlories" style="height: 200px">
            <span class="categlory-header">หมวดหมู่</span>
            <v-divider style="margin: 5px 0px 20px 0px"></v-divider>
            <div class="auto-tag-field">
              <v-autocomplete
                v-model="recipeDetail.RecipeTag"
                chips
                deletable-chips
                outlined
                multiple
                :items="states"
                :readonly="!isEditing"
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
                      placeholder="ใส่เวลาเตรียม"
                      v-model="recipeDetail.serve"
                      @blur="AddPrepTime"
                    >
                    </v-text-field>
                  </div>
                  <div class="prep-time-select">
                    <v-select
                      :items="prep"
                      label="เวลา"
                      solo
                      v-model="recipeDetail.serve"
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
                      placeholder="ใส่เวลาทำ"
                      v-model="recipeDetail.serve"
                    >
                    </v-text-field>
                  </div>
                  <div class="cook-time-select">
                    <v-select
                      :items="cookTime"
                      label="เวลา"
                      solo
                      v-model="recipeDetail.serve"
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
                      v-model="recipeDetail.Serve"
                    >
                    </v-text-field>
                  </div>
                </div>
              </div>
              <div class="recipe-data" style="display: block">
                <span>จำนวน :</span>
                <div class="for-yield">
                  <div class="yield-input">
                    <v-text-field
                      solo
                      placeholder="จำนวน"
                      v-model="recipeDetail.serve"
                    >
                    </v-text-field>
                  </div>
                  <div class="yield-select">
                    <v-text-field solo v-model="recipeDetail.serve">
                    </v-text-field>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Ingredients Text area -->

          <div class="field-recipe-ingredients">
            <span class="ingredients-header">ส่วนผสม</span>
            <v-divider style="margin: 5px 0px 20px 0px"></v-divider>
            <v-sheet
              class="sheet-ingredients"
              v-for="ingred in Ingredients"
              :key="ingred.id"
            >
              <div class="ingredients-field">
                <div class="input-name">
                  <v-text-field
                    :id="ingred.text"
                    v-model="ingred.text"
                    :value="ingred.text"
                    outlined
                    clearable
                    placeholder="เช่น น้ำมะนาว"
                    style="margin: 15px 0px 15px 0px"
                    @blur="addIngredbeforePost"
                  ></v-text-field>
                </div>
                <div class="input-unit" style="width: 40%">
                  <v-text-field
                    :id="ingred.unit"
                    v-model="ingred.unit"
                    :value="ingred.unit"
                    outlined
                    clearable
                    placeholder="เช่น 2 ช้อนโต๊ะ"
                    style="margin: 15px 0px 15px 20px"
                    @blur="addIngredbeforePost"
                  ></v-text-field>
                </div>
                <div class="action">
                  <span class="delete-directions" @click="deleteStep"
                    ><v-icon
                      @click="deleteIngredient"
                      style="margin-top: 28px; margin-left: 10px"
                      >delete</v-icon
                    ></span
                  >
                </div>
              </div>
            </v-sheet>

            <div
              class="btn-add-line-ingred"
              style="margin: 20px; display: flex; justify-content: center"
            >
              <v-btn @click="addIngred" outlined color="success"
                ><span><v-icon>add</v-icon></span> เพิ่มส่วนผสม</v-btn
              >
            </div>
          </div>

          <!-- directions text area -->

          <div class="field-recipe-directions">
            <span class="directions-header">วิธีทำ</span>
            <v-divider style="margin: 5px 0px 20px 0px"></v-divider>
            <v-sheet
              class="sheet-directions"
              v-for="(step, index) in steps"
              :key="step.id"
            >
              <div
                class="directions-field"
                style="position: relative; height: 50px"
              >
                <div
                  class="directions-item-label"
                  v-if="!step.editing"
                  @dblclick="editStep(step)"
                >
                  <v-divider
                    v-if="index !== 0"
                    :key="`${index}-divider`"
                    style="margin: 15px 0px 15px 0px; width: 100%"
                  ></v-divider>

                  <div
                    class="text-label"
                    style="display: flex; justify-content: space-between"
                  >
                    <span style="margin-left: 10px">{{ step.text }}</span>
                    <span class="delete-directions" @click="deleteStep"
                      ><v-icon>delete</v-icon></span
                    >
                  </div>
                </div>

                <div v-else class="directions-item-edit">
                  <v-text-field
                    autofocus
                    outlined
                    clearable
                    @blur="doneEditStep(step)"
                    @keydown.enter="doneEditStep(step)"
                    v-model="step.text"
                    style="margin: 0px"
                  ></v-text-field>
                </div>
              </div>
            </v-sheet>

            <v-text-field
              v-model="newStep"
              outlined
              clearable
              placeholder="เช่น น้ำมะนาว 2 ช้อนโต๊ะ"
              @keydown.enter="createStep"
              style="margin-top: 25px"
            ></v-text-field>
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
  </div>
</template>

<script>
// import AddIngred from '~/components/AddRecipe/AddIngred';
import axios from 'axios'

export default {
  components: {},

  data: () => ({
    isEditing: true,
    model: null,
    states: [
      'ไข่ดาว',
      'ไข่เจียว',
      'ต้มยำกุ้ง',
      'กะเพราหมูสับ',
      'เบอร์เกอร์',
      'ก๋วยเตี๋ยว',
    ],
    prep: ['นาที', 'ชั่วโมง', 'วัน'],
    cookTime: ['นาที', 'ชั่วโมง', 'วัน'],
    idIngred: 0,
    Ingredients: [
      {
        id: 0,
        text: 'น้ำปลา',
        unit: '2 ช้อนโต๊ะ',
      },
    ],
    newIngred: null,
    newUnit: null,

    idStep: 0,
    steps: [],
    newStep: null,
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

    DataRecipe: {
      title: null,
      photo_recipe: 'https://img.freepik.com/free-photo/board-amidst-cooking-ingredients_23-2147749529.jpg',
      description: null,
      RecipeTag: null,
      PrepTime: {
        num: null,
        unit: null,
      },
      CookTime: {
        num: null,
        unit: null,
      },
      serve: null,
      Yield: {
        num: null,
        unit: null,
      },
      Ingredients: [],
      Directions: [],
    },
  }),

  methods: {
    async getDataRecipe(rid) {
      this.$store.commit('SET_DIALOG_LOADING', true)
      var rid = this.$route.query.rid
      await axios.get('http://127.0.0.1:5000/api/recipe/' + rid).then((res) => {
        this.recipeDetail = res.data
        console.log(res.data)
      })
      this.$store.commit('SET_DIALOG_LOADING', false)
    },

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

    addIngred() {
      this.Ingredients.push({
        text: this.newIngred,
        unit: this.newUnit,
      })

      this.idIngred++
      console.log(this.Ingredients)
      this.DataRecipe.Ingredients = this.Ingredients.slice(
        0,
        this.Ingredients.length - 1
      )
    },

    addIngredbeforePost() {
      this.DataRecipe.Ingredients = this.Ingredients
      console.log(this.Ingredients)
    },

    deleteIngredient(index) {
      this.Ingredients.splice(index, 1)
      this.DataRecipe.Ingredients = this.Ingredients
      console.log(this.Ingredients)
    },

    createStep() {
      this.steps.push({
        id: this.idStep,
        text: this.newStep,
        editing: false,
      })

      this.idStep++
      this.newStep = null
      this.DataRecipe.Directions = this.steps
      console.log(this.steps)
    },

    deleteStep(index) {
      this.steps.splice(index, 1)
      console.log(this.steps)
    },

    editStep(step) {
      step.editing = true
    },
    doneEditStep(step) {
      step.editing = false
    },

    saveRecipeData(recipe_id) {
      // event.preventDefault()
      axios
        .put('http://127.0.0.1:5000/api/recipe/edit/' + recipe_id)
        .then((res) => {
          console.log(res)
        })
      console.log(this.DataRecipe)
    },
  },
  mounted() {
    this.getDataRecipe(this.rid)
  },
}
</script>

<style lang="scss">
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
  // margin: 25px 25px;
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


