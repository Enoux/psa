<script>
	import background from '$lib/assets/background.png';
</script>

<div
	class="relative m-4 flex h-[calc(100dvh-7rem)] flex-col justify-center gap-3 overflow-hidden rounded-3xl bg-foodpandapinklight px-20 text-foodpandablack"
>
	<img src={background} alt="Fast Food" class="absolute inset-0 h-full w-full object-cover" />

	<h1
		class="z-5 bg-linear-to-r/oklch from-pink-500 to-rose-500 bg-clip-text text-7xl font-extrabold text-transparent"
	>
		Food Pangmasa
	</h1>
	<p class="z-5 w-2/3 text-2xl">
		A project that seeks to plot out the trends in the average ratings and variety of restaurants,
		available on Foodpanda, in different cities with varying levels of urbanization nationwide.
	</p>
</div>
