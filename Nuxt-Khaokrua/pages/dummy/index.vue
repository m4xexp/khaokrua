<template>
  <v-container>
    <v-row>
      <v-col md="4" v-for="n in 6" :key="n">
        <v-sheet :color="`grey lighten-4`" class="pa-3">
          <v-skeleton-loader
            class="mx-auto"
            max-width="300"
            type="card"
          ></v-skeleton-loader>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    testItem: [
      'ITEM1001',
      'ITEM1002',
      'ITEM1003',
      'ITEM1004',
      'ITEM1005',
      'ITEM1006',
    ],
    preset: [
      {
        item_id: 'ITEM1001',
        src:
          'https://www.khaosod.co.th/wpapp/uploads/2020/09/animals-cats-cute-696x391.jpg',
        title: 'CAT',
      },
      {
        item_id: 'ITEM1002',
        src:
          'https://www.thairath.co.th/media/dFQROr7oWzulq5FZUIVRcfRXjBom9hQHg1XqIVqzfrpmV49b2XaDESbj8i6zjwyDm9i.jpg',
        title: 'JAI',
      },
      {
        item_id: 'ITEM1003',
        src: 'https://www.bth.co.th/images/news-health/pet.jpg',
        title: 'JAA',
      },
      {
        item_id: 'ITEM1004',
        src:
          'https://cache.gmo2.sistacafe.com/images/uploads/summary/image/2879/1441953470-Animal-HD-Wallpapers.jpg',
        title: 'BAM',
      },
      {
        item_id: 'ITEM1005',
        src:
          'https://image.bangkokbiznews.com/kt/media/image/fileupload1/source/159854958962.jpg?1598549590262',
        title: 'MAX',
      },
      {
        item_id: 'ITEM1006',
        src:
          'https://thonglorpet.com/public/upload/pet-diary/vet%20tips/OGQEOC0.jpg',
        title: 'PRIEW',
      },
    ],
    touch: [],
  }),
  methods: {
    logItem(id) {
      console.log(id)
      this.touch.push(id)
      console.log('This is work', this.touch)
    },
  },
}
</script>

<style scoped>
</style>