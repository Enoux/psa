<script>
	import { slide } from 'svelte/transition';
	import MLScatterPlot from '$lib/graphs/ml_scatter_plot.png';

	let methods = $state(false);

	const methodContent = [
		{
			title: 'Data Collection and Collation',
			icon: 'icon-[mdi--restaurant]',
			class: 'text-lg',
			content:
				'The following columns were collected from the restaurants dataset for the model training:<br><span class="w-full font-medium">Food Type, City, & Average Rating</span>'
		},

		{
			title: 'Data Encoding and Transformation',
			icon: 'icon-[fluent--code-16-filled]',
			class: 'text-lg',
			content:
				'The Food Type category was transformed using <span class="font-medium">One-Hot Encoding</span> & each City entry was <span class="font-medium">replaced by its corresponding population density</span>. The Average Ratings remained as is.'
		},

		{
			title: 'Model Selection and Training',
			icon: 'icon-[mdi--computer]',
			class: 'text-sm',
			content:
				'Since the <span class="font-medium">dependent variable is continuous but the data is very skewed</span>, it is best to use regression models that account for this (i.e. Decision Tree Regressors & Random Forest Regressors).<br><br>The data was then <span class="font-medium">split 80-20</span> & the models were fitted accordingly.'
		},

		{
			title: 'Hyperparameter Tuning',
			icon: 'icon-[mdi--tools]',
			class: '',
			content:
				'For the Decision Tree Regressor, its <span class="font-medium">ccp-alphas</span> were all tested to see which one would produce the most optimal result--1.14537<sup>-7</sup> was obtained which improved the performance of the model (R<sup>2</sup>) by around <span class="font-medium">10%</span>.'
		}
	];
</script>

<div class="mx-24 mt-4 mb-8 flex flex-col place-content-center">
	<h3 class="mb-8 w-full text-3xl font-bold">Machine Learning (Modelling)</h3>

	<p class="w-full px-36 text-center text-lg">
		Using the restaurant data from Foodpanda, we trained a <span class="font-bold"
			>Decision Tree Regressor</span
		>
		and a
		<span class="font-bold">Random Tree Regressor</span> to predict the
		<span class="font-bold">average rating of a restaurant</span>
		based on its type and the urbanization (i.e. the
		<span class="italic">population density</span>)) of its location.
	</p>

	<!-- Limitations -->
	<div class="flex w-full flex-row flex-wrap place-content-center">
		<div
			class="m-10 flex w-2/5 flex-row flex-wrap place-content-center rounded-xl bg-foodpandapink px-16 py-4 text-foodpandagraylight"
		>
			<h4 class="mb-8 w-full text-center text-3xl font-semibold">Limitations</h4>
			<div class="mb-4 w-full text-center">
				As can be seen in the scatter plot on the right, the dataset is <span class="font-bold"
					>skewed heavily to the higher ratings</span
				>--there is an overwhelming amount of above 4.5, especially 5.0, average ratings.
			</div>

			<div class="w-1/2 rounded-xl p-4 text-center">
				As a result, the data only has:<br />
				<span class="text-3xl font-bold">0.053168</span><br />
				variance
			</div>

			<div class="w-1/2 rounded-xl p-4 text-center">
				There are only<br />
				<span class="text-3xl font-bold">17 cities</span><br />
				leading to vertical lines in the scatter plot
			</div>
		</div>
		<div class="flex place-content-center p-10">
			<img src={MLScatterPlot} alt="Scatter Plot of Data used for Training of ML Models" />
		</div>
	</div>

	<!-- Methods -->
	<div class="flex w-full flex-wrap place-content-center gap-10 px-16 text-center">
		{#each methodContent as method (method)}
			<div
				class="flex w-1/5 flex-col flex-wrap rounded-xl bg-foodpandapinklight p-4"
				onmouseenter={() => (methods = true)}
				onmouseleave={() => (methods = false)}
				role="tooltip"
			>
				<div class="w-full">
					<span class="{method.icon} text-6xl"></span>
					<h4 class="text-2xl font-bold {methods ? 'mb-2' : ''}">{method.title}</h4>
				</div>
				{#if methods}
					<div transition:slide class="flex w-full flex-wrap place-content-center">
						<p class={method.class}>
							{@html method.content}
						</p>
					</div>
				{/if}
			</div>
		{/each}
	</div>

	<!-- Results -->
	<div class="flex w-full flex-row flex-wrap place-content-center text-foodpandagraylight">
		<div
			class="m-10 flex w-2/5 flex-wrap place-content-center rounded-xl bg-foodpandapink p-8 text-center"
		>
			<h4 class="mb-4 w-full text-3xl font-bold">Decision Tree Regressor</h4>
			<p class="w-full text-xl">Mean Absolute Error (MAE): <span class="font-bold">0.105</span></p>
			<p class="w-full text-xl">
				R-squared (R<sup>2</sup>): <span class="font-bold">0.08350</span>
			</p>
		</div>

		<div
			class="m-10 flex w-2/5 flex-wrap place-content-center rounded-xl bg-foodpandapink p-8 text-center"
		>
			<h4 class="mb-4 w-full text-3xl font-bold">Random Forest Regressor</h4>
			<p class="w-full text-xl">Mean Absolute Error (MAE): <span class="font-bold">0.112</span></p>
			<p class="w-full text-xl">
				R-squared (R<sup>2</sup>): <span class="font-bold">0.08357</span>
			</p>
		</div>
	</div>

	<!-- Interpretation & Conclusion for ML? -->
	<div class="flex w-full place-content-center">
		<div class="flex w-4/5 flex-wrap rounded-2xl bg-foodpandapinklight p-10 text-center">
			<div class="flex w-1/2 flex-wrap px-8">
				<p class="w-full">With an R<sup>2</sup> of around 0.08, the model is able to account for</p>
				<p class="w-full text-3xl font-bold">8% of the variance</p>
				<p class="w-full">in the data and make predictions for this portion accurately</p>
			</div>
			<div class="flex w-1/2 flex-wrap px-8">
				<p class="w-full">Meanwhile, the MAE implies that the predictions are off by</p>
				<p class="w-full text-3xl font-bold">
					0.105 and 0.112 <span class="icon-[solar--star-bold] text-2xl"></span>
				</p>
				<p class="w-full">for the Decision Tree & Random Forest models, respectively</p>
			</div>

			<div class="flex w-full px-10 pt-8">
				<p class="w-full">
					Though the accuracy of the model might be low, it can still be used to gain valuable
					insights on the<br />
					<span class="text-lg font-bold"
						>trends of restaurants' perceived quality (via ratings) based on their type & location</span
					>.
				</p>
			</div>
		</div>
	</div>
</div>
