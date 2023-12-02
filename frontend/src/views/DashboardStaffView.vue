<template>
  <div class="logout">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <DashboardTable/>
  </div>
</template>

<script>
import DashboardTable from '@/components/DashboardTable.vue';

export default {
  name: 'DashboardStaffView',
  components: {
    DashboardTable
  }
}
</script>
