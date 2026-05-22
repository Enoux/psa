<script>
	const sections = [
		{ name: 'Overview', path: '#overview', icon: 'icon-[fluent--search-16-filled]' },
		{ name: 'Results', path: '#results', icon: 'icon-[solar--graph-bold]' },
		{ name: 'Modelling', path: '#modelling', icon: 'icon-[mdi--computer-classic]' },
		{ name: 'Team', path: '#team', icon: 'icon-[fluent--people-team-16-filled]' }
	];

	import { resolve } from '$app/paths';
	import graphRestoCountUrbanized from '$lib/graphs/barchart_restoCount_highly_urbanized.png';
	import graphRestoCountRural from '$lib/graphs/barchart_restoCount_rural.png';
	import graphHistoUrbanized from '$lib/graphs/histogram_highly_urbanized.png';
	import graphHistoRural from '$lib/graphs/histogram_rural.png';
	import Results from '$lib/Results.svelte';
	import About from '$lib/About.svelte';
	import Modelling from '$lib/Modelling.svelte';
	import Title from '$lib/Title.svelte';
	import Overview from '$lib/Overview.svelte';

	/** @type {Record<string, string>} */
	const graphs = import.meta.glob('$lib/graphs/FoodType_*.png', {
		eager: true,
		import: 'default'
	});

	const cities = [
		'Cebu',
		'Dagupan',
		'Davao',
		'Koronadal',
		'Lapulapu',
		'Makati',
		'Malolos',
		'Mandaluyong',
		'Manila',
		'Marikina',
		'Muntinlupa',
		'Ormoc',
		'Pasay',
		'Pasig',
		'QuezonCity',
		'SanJuan',
		'Taguig',
		'Valencia'
	];

	const cityGraphs = cities.map((city) => {
		const path = `/src/lib/graphs/FoodType_${city}.png`;
		return {
			city,
			src: graphs[path]
		};
	});
</script>

<div
	class="navbar sticky top-0 z-10 flex h-[5rem] w-full items-center justify-between gap-10 bg-white px-20 shadow-lg/8"
>
	<a href={resolve('/')} class="text-3xl font-medium text-nowrap text-pink-500">
		<span class="icon-[mdi--bar-chart] align-text-bottom text-4xl"></span>
		Food Pangmasa
	</a>

	<div class="flex h-full gap-3">
		{#each sections as section (section.name)}
			<a
				href={section.path}
				class="group flex items-center justify-center gap-2 rounded-sm px-4 text-foodpandagray transition-colors hover:bg-foodpandagraylight hover:text-foodpandablack"
			>
				<span class="{section.icon} text-2xl"></span>
				<p>{section.name}</p>
				<span
					class="absolute bottom-0.5 h-1 w-0 rounded-xl bg-foodpandablack transition-all duration-75 group-hover:w-8"
				></span>
			</a>
		{/each}
	</div>
</div>

<Title />

<section id="overview" class="scroll-mt-24">
	<Overview></Overview>
</section>

<div class="px-40 text-foodpandablack">
	<section id="results" class="scroll-mt-24">
		<Results />
	</section>

	<section id="results" class="scroll-mt-24">
		<!-- <h2 class="text-xl font-bold">Exploratory Data Analysis</h2>

		<p class="font-bold">
			1. Does the urbanization of a city have an effect on the quality of food served by
			restaurants/shops on delivery service platforms, such as Foodpanda?
		</p>

		<div class="text-l flex justify-center gap-3 px-20 py-5 text-center">
			<div class="w-full rounded-lg bg-foodpandapink p-3 text-white">
				<p class="mb-3 text-xl font-bold">Null Hypothesis</p>
				There is no significant difference between the quality of food of restaurants available on Foodpanda
				in urban and rural cities.
			</div>
			<div class="w-full rounded-lg bg-foodpandapink p-3 text-white">
				<p class="mb-3 text-xl font-bold">Alternative Hypothesis</p>
				There is a significant difference between the quality of food of restaurants in urban and rural
				cities.
			</div>
		</div>

		<div class="mx-10">
			<p>
				Higher ratings of restaurants on FoodPanda correspond to higher quality of food. An <strong
					>independent samples t-test</strong
				> was used to test the null hypothesis because it compares two types of cities—highly urbanized
				and rural—and the average ratings of restaurants found in the two groups.
			</p>

			The distribution of restaurants per type of city is as follows:
			<ul class="ml-5 list-inside list-disc">
				<li>Total number of restaurants in highly urbanized cities: <strong> 8656 </strong></li>
				<li>Total number of restaurants in rural cities: <strong> 716 </strong></li>
			</ul>

			<p>
				Breaking down the distribution of restaurants per city (grouped by highly urbanized vs
				rural):
			</p>

			<div class="flex w-full flex-wrap justify-center gap-20 py-5">
				<img
					src={graphRestoCountUrbanized}
					alt="Distribution of Restaurants Per Highly Urbanized City"
					class="h-auto max-w-full min-w-[300px] flex-1"
				/>
				<img
					src={graphRestoCountRural}
					alt="Distribution of Restaurants Per Rural City"
					class="h-auto max-w-full min-w-[300px] flex-1"
				/>
			</div>

			<p>
				The t-test assumes that the data are normally distributed for the analysis to be valid.
				Graphing the histograms of the distribution of ratings per city type yields the following:
			</p>

			<div class="flex w-full flex-wrap justify-center gap-20 py-5">
				<img
					src={graphHistoUrbanized}
					alt="Histogram of the Distribution of Ratings in Highly Urbanized Cities"
					class="h-auto max-w-full min-w-[300px] flex-1"
				/>
				<img
					src={graphHistoRural}
					alt="Histogram of the Distribution of Ratings in Rural Cities"
					class="h-auto max-w-full min-w-[300px] flex-1"
				/>
			</div>

			<p>
				The graphs appear to be heavily skewed on the right, violating the normal distribution
				assumption. Moreover, applying the <strong> Shapiro-Wilk Test </strong> on the data for highly
				urbanized and rural cities yielded extremely small p-values (&lt;0.05). This indicates that the
				dataset deviate from normality. It is important to also note that Shapiro-Wilk Test is best for
				sample sizes of at most 5000. Hence, the Shapiro-Wilk test for highly urbanized cities may yield
				a less accurate result.
			</p>

			<div class="m-3 ml-10 space-y-3">
				<p>
					Shapiro-Wilk Test for Highly Urbanized Cities: <br />
					Test Statistic: 0.3435944633235567 <br />
					p-value: 1.866337625580115e-100 <br />
				</p>

				<p>
					Shapiro-Wilk Test for Less Urbanized Cities: <br />
					Test Statistic: 0.3930989623886074 <br />
					p-value: 1.6335223148222224e-43 <br />
				</p>
			</div>

			<p>
				However, the <strong> Central Limit Theorem </strong> states that with more than 30 samples, the
				samples’ means will converge to a normal distribution despite the original variables not being
				normally distributed.
			</p>

			<p>Applying the t-test gives the following results:</p>

			<p class="m-3 ml-10">
				Independent Samples t-test: <br />
				t-statistic: 0.0931349185318071 <br />
				p-value: 0.9257983682059079 <br />
			</p>

			<p>
				The p-value is much greater than 0.05, hence it <strong
					>fails to reject the null hypothesis.</strong
				> Using a non-parametric statistical test for data that is not normally distributed corroborates
				this result:
			</p>

			<p class="m-3 ml-10">
				Mann-Whitney U Test: <br />
				U-statistic: 3130783.0 <br />
				p-value: 0.5888579822174669 <br />
			</p>
		</div>

		<p class="font-bold">
			2. What are the most commonly ordered cuisine/food/drink types (e.g. Fast Food, Filipino,
			etc.), based on the amount of reviews & reviewers, in cities of varying levels of
			urbanization?
		</p>

		<div class="mx-10">
			<p>
				Users from highly urbanized cities/regions are likely to order more varied types of food,
				while fast food may be more commonly ordered in other areas.
			</p>

			<p>
				Based on the graphs generated for the Foodpanda restaurant types (e.g. Filipino, Chicken,
				Japanese, etc.) in each city in the dataset, it can be observed that the non-highly
				urbanized cities (i.e. Ormoc, Malolos, Dagupan, Koronadal, & Valencia) all have <strong>
					Fast Food
				</strong> as the type of restaurant most ordered from (based on user reviews), by an overwhelming
				margin, in those cities.
			</p>
		</div>

		<div class="flex gap-6 overflow-x-auto">
			{#each cityGraphs as { city, src } (city)}
				<div class="min-w-[300px]">
					<img {src} alt={`graph ${city}`} class="h-auto w-full" />
				</div>
			{/each}
		</div> -->
	</section>

	<br />
</div>

<section id="modelling" class="scroll-mt-24">
	<Modelling />
</section>

<section id="team" class="scroll-mt-24">
	<About />
</section>
