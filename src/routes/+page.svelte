<script>
	const sections = [
		{ name: 'Home', path: '#' },
		{ name: 'Background', path: '#background' },
		{ name: 'About', path: '#about' }
	];
</script>

<div class="navbar sticky top-0 flex flex-wrap w-full justify-center items-center gap-3 bg-white shadow-md">
	<div class="flex font-bold text-3xl text-foodpandapink px-5">
		PSA
	</div>
	{#each sections as section}
		<a
			href={section.path}
			class="text-foodpandagray hover:bg-foodpandapink hover:text-white rounded-sm p-4 transition-colors"
		>
			{section.name}
		</a>
	{/each}
</div>

<div class ="text-foodpandablack p-4">


	<h1 class="text-5xl font-bold text-foodpandapink text-center">Food Pangdamasa</h1>

	<br />

	<h2 class="text-2xl font-semibold text-center">SDG 2: Zero Hunger</h2>

	<br />

	<section id= "background" class="background scroll-mt-16">
		<h2 class="text-xl font-bold">Problem & Background</h2>
		<p>
			Foodpanda is an online food delivery platform that is widely used in the Philippines, especially
			in recent years. Many customers turn to Foodpanda to have their food delivered from a range of
			restaurants and stores available on the platform. Because of the nature of delivery services,
			customers are still limited to the food options available in their local area. As such, users from
			some cities may have convenient access to a wide range of highly satisfactory food while others
			might not be able to avail of the same variety and quality in their area.
		</p>

		<br />

		<h2 class="text-xl font-bold">Solution</h2>
		<p>
			To address this, a comprehensive analysis of the reviews left by Food Panda customers will be done
			to gain a better understanding of food widely available and sought after in different cities. In
			doing so, attention may be turned to areas that can still improve on the quality and variety of
			available food on delivery service platforms such as Foodpanda.
		</p>

		<br />

		<h2 class="text-xl font-bold">Research Questions</h2>
		<ol>
			<li>
				Does the urbanization of a city have an effect on the quality of food served by
				restaurants/shops on delivery service platforms, such as Foodpanda?
			</li>
			<li>
				What are the most commonly ordered cuisine/food/drink types (e.g. Fast Food, Filipino, etc.),
				based on the amount of reviews & reviewers, in cities of varying levels of urbanization?
			</li>
		</ol>

		<br />

		<h2 class="text-xl font-bold">Research Hypotheses</h2>
		<ol>
			<li>Highly urbanized cities/regions are likely to have higher quality restaurants and shops.</li>
			<li>
				Users from highly urbanized cities/regions are likely to order more varied types of food, while
				fast food may be more commonly ordered in other areas.
			</li>
		</ol>

		<br />

		<h2 class="text-xl font-bold">Objectives</h2>
		<ol>
			<li>
				Determine if there is a correlation between the urbanization of a city/region to the quality of
				the food they can order online.
			</li>
			<li>Identify the types of food that Filipinos primarily order online.</li>
		</ol>

		<br />

		<h2 class="text-xl font-bold">Important Links</h2>
		<ol>
			<li>
				<a
					href="https://docs.google.com/spreadsheets/d/1CkC7lJ7P7uGn0Js8b4sufUD3CL3NthUVe_2WrZq40d8/edit?usp=sharing"
					class="text-green-800 underline"
					target="_blank"
				>
					Uploaded Dataset (GSheets)
				</a>
			</li>
			<li>
				<a
					href="https://docs.google.com/document/d/1j4aIZpcoBELYkqf5x0IA8JUSZ3Fl8aTrHh3rioMdGEc/edit?tab=t.uuf2zm7zpj7i#heading=h.6fr3l6ulkshz"
					class="text-blue-800 underline"
					target="_blank"
				>
					Dataset Description (GDocs)
				</a>
			</li>
		</ol>
	</section>

	<br />

	<section id="about">
		<h2 class="text-xl font-bold"> About Us </h2>
		<div class="text-l flex gap-3 justify-center px-20 py-5 text-center">
			<div class="w-full">DOMINGO, Karlo S.</div>
			<div class="w-full">LAZARO, Benjeouelle A.</div>
			<div class="w-full">MORACA, Phoebe Renee P.</div>
		</div>
	</section>

</div>
