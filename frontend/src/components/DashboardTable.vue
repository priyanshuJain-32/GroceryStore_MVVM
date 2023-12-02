<template>
    <div class="products-table">

		<table id = "product-table" class="table" style="width: 95%; text-align: center;">
			<th>Request Id</th>
			<th>Request Type</th>
			<th>Request Status</th>
			<th v-if="params.role == 'admin'">Requester Id</th>
			<th v-if="params.role == 'admin'"></th>
			<th v-if="params.role == 'admin'"></th>
			
			<tr v-for="request in requests.requests" :key="request.request_id">
				<td>{{ request.request_id }}</td>
				<td>{{ request.request_type }}</td>
				<td>{{ request.request_status }}</td>
				<td>{{ request.requester_id }}</td>
				<td v-if="params.role=='admin'">
					<label for="request_action"><b>Action</b></label> |
					<select v-model="requestToChange.request_status" @click="updateStatus(request)" name="request_status" required>
						<option value="approve">Approve</option>
						<option value="reject">Reject</option>
					</select>
				</td>
				<td v-if="params.role=='admin'">
					<form>
						<input type="button" @click="this.deleteRequest(request)" style="width: 150px;" name="delete_request" value = "Delete Request"/>
					</form>
				</td>
			</tr>
		</table>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex';
export default {
  name: 'DashboardTable',
  computed: {
    ...mapGetters('auth',['params']),
	...mapGetters('request',['requestToChange', 'requests'])
  },
  methods: {
	updateStatus(request){
		this.alterRequestState(request)
		this.alterRequestStatus(this.requestToChange)
		this.putRequest()
	},
	...mapMutations('request',['alterRequestState','alterRequestStatus']),
	...mapActions('request',['raiseRequest', 'deleteRequest','putRequest'])
  },
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
