<script>
	import graphRestoCountDistrib from '$lib/graphs/barchart_restoCountDistrib.png';
	import graphRestoCountUrbanized from '$lib/graphs/barchart_restoCount_highly_urbanized.png';
	import graphRestoCountRural from '$lib/graphs/barchart_restoCount_rural.png';
	import graphHistoUrbanized from '$lib/graphs/histogram_highly_urbanized.png';
	import graphHistoRural from '$lib/graphs/histogram_rural.png';
</script>

<div class="m-4 mb-8 flex flex-col place-content-center text-foodpandablack">
	<!-- header -->
	<div class="flex w-full flex-row items-center space-x-4">
		<span class="icon-[solar--graph-bold] text-3xl text-foodpandapink"></span>
		<p
			class="bg-linear-to-r/oklch from-pink-500 to-rose-500 bg-clip-text text-4xl font-extrabold text-transparent"
		>
			Exploratory Data Analysis
		</p>
	</div>

	<p class="w-full pt-2 pb-2 text-2xl">Urbanization and Food Quality</p>

	<p class="w-full text-justify text-lg">
		Higher ratings of restaurants on FoodPanda correspond to higher quality of food. An independent
		samples t-test was used to test the null hypothesis because it compares two types of
		cities—highly urbanized and rural—and the average ratings of restaurants found in the two
		groups.
	</p>

	<div class="flex w-full place-content-center">
		<img
			src={graphRestoCountDistrib}
			alt="Distribution of Restaurants Per City Type"
			class="h-auto w-xl pt-2 pb-2"
		/>
	</div>

	<p class="pt-2 pb-4 text-lg">
		The following displays the full breakdown of the distribution of restaurants per type of city.
	</p>

	<div class="grid grid-cols-2">
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

	<p class="pb-4 text-lg">
		The t-test assumes that the data are normally distributed for the analysis to be valid. Graphing
		the histograms of the distribution of ratings per city type yields the following:
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
	<p class="pb-4 text-lg">
		The graphs appear to be heavily skewed on the right, violating the normal distribution
		assumption. Moreover, applying the Shapiro-Wilk Test on the data for highly urbanized and rural
		cities yielded extremely small p-values (less than 0.05). This indicates that the dataset
		deviate from normality. It is important to also note that Shapiro-Wilk Test is best for sample
		sizes of at most 5000. Hence, the Shapiro-Wilk test for highly urbanized cities may yield a less
		accurate result.
	</p>

	<div class="flex place-content-center">
		<table class="w-3xl table-auto border-collapse">
			<caption class="caption-bottom"> Shapiro-Wilk Test Results </caption>
			<tbody>
				<tr>
					<th></th>
					<th class="place-content-center border-b-2 p-2"> Highly Urbanized Cities </th>
					<th class="border-b-2 p-2"> Rural Cities </th>
				</tr>
				<tr>
					<th class="border-r-2 p-2"> Test Statistic</th>
					<td class="border-2 p-2 text-center"> 0.3435944633235567 </td>
					<td class="border-2 p-2 text-center"> 0.3930989623886074 </td>
				</tr>
				<tr>
					<th class="border-r-2 p-2"> p-value</th>
					<td class="border-2 p-2 text-center"> 1.866337625580115e-100</td>
					<td class="border-2 p-2 text-center"> 1.6335223148222224e-43</td>
				</tr>
			</tbody>
		</table>
	</div>

	<p class="pt-4 pb-4 text-lg">
		However, the Central Limit Theorem states that with more than 30 samples, the samples’ means
		will converge to a normal distribution despite the original variables not being normally
		distributed. Applying the t-test gives the following results:
	</p>

	<div class="flex w-full place-content-center">
		<div class="flex w-4/5 flex-wrap rounded-2xl bg-foodpandapinklight p-4 text-center">
			<div class="flex w-1/2 flex-wrap px-8">
				<p class="w-full">t-statistic</p>
				<p class="w-full text-2xl font-bold">0.0931349185318071</p>
			</div>
			<div class="flex w-1/2 flex-wrap px-8">
				<p class="w-full">p-value</p>
				<p class="w-full text-2xl font-bold">0.9257983682059079</p>
			</div>

			<div class="flex w-full pt-4">
				<p class="w-full">
					The p-value is much greater than 0.05, hence it <span class="font-bold">
						fails to reject
					</span> the null hypothesis (RQ1).
				</p>
			</div>
		</div>
	</div>

	<p class="pt-4 pb-4 text-lg">
		Using Mann-Whitney U Test, a non-parametric statistical test for data that is not normally
		distributed, corroborates this result:
	</p>

	<div class="flex w-full place-content-center">
		<div class="flex w-4/5 flex-wrap rounded-2xl bg-foodpandapinklight p-4 text-center">
			<div class="flex w-1/2 flex-wrap px-8">
				<p class="w-full">U-statistic</p>
				<p class="w-full text-2xl font-bold">3130783.0</p>
			</div>
			<div class="flex w-1/2 flex-wrap px-8">
				<p class="w-full">p-value</p>
				<p class="w-full text-2xl font-bold">0.5888579822174669</p>
			</div>
		</div>
	</div>

	<p class="w-full pt-10 pb-2 text-2xl">Urbanization and Food Variety</p>

	<p class="w-full text-justify text-lg">
		By tallying the restaurant types per city, the following graphs can be obtained wherein the
		cities are grouped based on whether or not they are a highly urbanized city (HUC) as classified
		by Phil Atlas:
	</p>
</div>
