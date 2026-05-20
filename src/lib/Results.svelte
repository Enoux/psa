<script>
	import graphRestoCountDistrib from '$lib/graphs/barchart_restoCountDistrib.png';
	import { CollapsibleCard } from 'svelte-collapsible';
	import graphRestoCountUrbanized from '$lib/graphs/barchart_restoCount_highly_urbanized.png';
	import graphRestoCountRural from '$lib/graphs/barchart_restoCount_rural.png';
	import graphHistoUrbanized from '$lib/graphs/histogram_highly_urbanized.png';
	import graphHistoRural from '$lib/graphs/histogram_rural.png';
</script>

<div class="flex items-center justify-center">
	<div class="flex w-3xl flex-col items-center justify-center space-y-4 rounded-xs bg-white p-10">
		<!-- header -->
		<div class="flex w-full flex-row items-center space-x-4">
			<span class="icon-[solar--graph-bold] text-3xl text-foodpandapink"></span>
			<p
				class="bg-linear-to-r/oklch from-pink-500 to-rose-500 bg-clip-text text-3xl font-extrabold text-transparent"
			>
				Exploratory Data Analysis
			</p>
		</div>

		<p class="w-full text-lg">Urbanization VS Food Quality</p>

		<!-- Hypotheses -->
		<div class="flex w-xl flex-row space-x-4">
			<div
				class="flex w-1/2 flex-col items-center justify-center rounded-xl border border-foodpandablack/30 p-2 text-center"
			>
				<p class="font-bold">Null Hypothesis</p>
				<p class="text-sm">
					There is no significant difference between the food quality of restaurants available on
					Foodpanda in urban and rural cities.
				</p>
			</div>
			<div
				class="flex w-1/2 flex-col items-center justify-center rounded-xl border border-foodpandablack/30 p-2 text-center"
			>
				<p class="font-bold">Alternative Hypothesis</p>
				<p class="text-sm">
					There is a significant difference between the food quality of restaurants in urban and
					rural cities.
				</p>
			</div>
		</div>

		<p class="text-justify">
			Higher ratings of restaurants on FoodPanda correspond to higher quality of food. An
			independent samples t-test was used to test the null hypothesis because it compares two types
			of cities—highly urbanized and rural—and the average ratings of restaurants found in the two
			groups.
		</p>
		<img
			src={graphRestoCountDistrib}
			alt="Distribution of Restaurants Per City Type"
			class="h-auto w-xl"
		/>
		<CollapsibleCard>
			<p class="w-full cursor-pointer rounded border bg-foodpandablack/15 p-2" slot="header">
				View further breakdown of the distribution of restaurants per city
			</p>
			<div slot="body">
				<img
					src={graphRestoCountUrbanized}
					alt="Distribution of Restaurants Per City Type"
					class="h-auto w-lg"
				/>
				<img
					src={graphRestoCountRural}
					alt="Distribution of Restaurants Per City Type"
					class="h-auto w-lg"
				/>
			</div>
		</CollapsibleCard>

		<p>
			The t-test assumes that the data are normally distributed for the analysis to be valid.
			Graphing the histograms of the distribution of ratings per city type yields the following:
		</p>
		<div class="flex space-x-2">
			<img
				src={graphHistoUrbanized}
				alt="Distribution of Restaurants Per City Type"
				class="h-auto w-1/2"
			/>

			<img
				src={graphHistoRural}
				alt="Distribution of Restaurants Per City Type"
				class="h-auto w-1/2"
			/>
		</div>
		<p>
			The graphs appear to be heavily skewed on the right, violating the normal distribution
			assumption. Moreover, applying the Shapiro-Wilk Test on the data for highly urbanized and
			rural cities yielded extremely small p-values (less than 0.05). This indicates that the
			dataset deviate from normality. It is important to also note that Shapiro-Wilk Test is best
			for sample sizes of at most 5000. Hence, the Shapiro-Wilk test for highly urbanized cities may
			yield a less accurate result.
		</p>

		<table class="table-auto border-collapse border">
			<tbody>
				<tr>
					<th class="border p-2"> Shapiro-Wilk Test </th>
					<th class="border p-2"> Highly Urbanized Cities </th>
					<th class="border p-2"> Rural Cities </th>
				</tr>
				<tr>
					<th class="border p-2"> Test Statistic</th>
					<td class="border p-2"> 0.3435944633235567 </td>
					<td class="border p-2"> 0.3930989623886074 </td>
				</tr>
				<tr>
					<th class="border p-2"> p-value</th>
					<td class="border p-2"> 1.866337625580115e-100</td>
					<td class="border p-2"> 1.6335223148222224e-43</td>
				</tr>
			</tbody>
		</table>

		<p>
			However, the Central Limit Theorem states that with more than 30 samples, the samples’ means
			will converge to a normal distribution despite the original variables not being normally
			distributed. Applying the t-test gives the following results:
		</p>
		<p>Independent Samples t-test: t-statistic: 0.0931349185318071 p-value: 0.9257983682059079</p>
		<p>
			The p-value is much greater than 0.05, hence it fails to reject the null hypothesis. Using a
			non-parametric statistical test for data that is not normally distributed corroborates this
			result: Mann-Whitney U Test: U-statistic: 3130783.0 p-value: 0.5888579822174669
		</p>
	</div>
</div>
