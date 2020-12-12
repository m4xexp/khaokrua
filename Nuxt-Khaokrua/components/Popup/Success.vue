<template>
    <v-dialog persistent v-model="success" width="500">
      <v-card>
        <v-card-title color="#00E676"> แจ้งเตือน </v-card-title>
        <v-card-text class="textDetail">
          {{ $store.getters.getDialogMsg }}
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="$store.dispatch({ type: 'successPopup', value: false, msg: '' })"
          >
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
export default {
  name: "successDialog"
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Kanit:wght@200&display=swap');


* {
  list-style: none;
  outline: none;
  font-family: 'Kanit', sans-serif;
  box-sizing: border-box;
}

.textDetail{
  font-size: 30px;
}
</style>
