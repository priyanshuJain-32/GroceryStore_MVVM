<template>
	<div v-if="params.role == 'admin'">
		<nav>
			<input type="button" @click="this.generateCsv('products')" style="width: 150px;" name="generate_products_csv" value = "Export Products csv"/>
			<input type="button" @click="this.generateCsv('categories')" style="width: 150px;" name="generate_categories_csv" value = "Export Categories csv"/>
			<input type="button" @click="this.generateCsv('orders')" style="width: 150px;" name="generate_orders_csv" value = "Export Orders csv"/>
			<input type="button" @click="this.generateCsv('users')" style="width: 150px;" name="generate_users_csv" value = "Export Users csv"/>
		</nav>
	</div>
	<br><br>
    <div class="products-table">
		<div v-if="Object.keys(requests.requests)[0] == 'message'">
		<h2>No requests to show</h2>
		</div>
		<div v-if="Object.keys(requests.requests)[0] !== 'message'">
		<table id = "product-table" class="table" style="width: 95%; text-align: center;">
			<th>Request Id</th>
			<th>Request Type</th>
			<th v-if="params.role == 'admin'">Requester Id</th>
			<th>Request Status</th>
			<th v-if="params.role == 'admin'"></th>
			<th v-if="params.role == 'admin'"></th>
			<th v-if="params.role == 'admin'"></th>
			
			<tr v-for="request in requests.requests" :key="request.request_id">
				<td>{{ request.request_id }}</td>
				<td>{{ request.request_type }}</td>
				<td v-if="params.role == 'admin'">{{ request.requester_id }}</td>
				<td>{{ request.request_status }}</td>
				<td v-if="(params.role=='admin') && (request.request_status == 'approve' || request.request_status == 'reject')"></td>
				<td v-if="(params.role=='admin') && (request.request_status !== 'approve' && request.request_status !== 'reject')">
					<form>
						<input type="button" @click="this.commitAlterRequest(request,'approve')" style="width: 150px;" name="approve_request" value = "Approve Request"/>
					</form>
				</td>
				<td v-if="(params.role=='admin') && (request.request_status == 'approve' || request.request_status == 'reject')"></td>
				<td v-if="params.role=='admin' && (request.request_status!= 'approve' && request.request_status!= 'reject')">
					<form>
						<input type="button" @click="this.commitAlterRequest(request, 'reject')" style="width: 150px;" name="reject_request" value = "Reject Request"/>
					</form>
				</td>
				<td v-if="params.role=='admin'">
					<form>
						<input type="button" @click="this.deleteRequest(request)" style="width: 150px;" name="delete_request" value = "Delete Request"/>
					</form>
				</td>
			</tr>
		</table>
	</div>
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
	commitAlterRequest(request, payload){
		this.alterRequestState(request)
		this.alterRequestStatus(payload)
		this.putRequest()
	},
	...mapMutations('request',['alterRequestState','alterRequestStatus']),
	...mapActions('request',['deleteRequest','putRequest']),
	...mapActions('jobs',['generateCsv'])
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
