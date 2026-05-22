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

</div>

<section id="modelling" class="scroll-mt-24">
	<Modelling />
</section>

<section id="team" class="scroll-mt-24">
	<About />
</section>
