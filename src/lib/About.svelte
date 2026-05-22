<script>
	import benj from '$lib/assets/benj.jpg';
	import fibi from '$lib/assets/fibi.jpg';
	import karlo from '$lib/assets/karlo.png';
</script>

<div class="m-4 rounded-3xl bg-foodpandapinklight py-10 text-foodpandablack">
	<h2 class="px-30 pb-10 text-3xl font-medium">
		<span class="icon-[fluent--people-team-16-filled] align-text-bottom text-4xl"></span> Team
	</h2>

	<div class="text-l flex justify-center gap-5 px-40">
		<div class="w-full gap-3">
			<img
				src={benj}
				alt="Benj Lazaro"
				class="mb-2 aspect-4/5 rounded-xl border border-foodpandapink/30 object-cover"
			/>
			<p class="text-xl font-bold">Benj Lazaro</p>

			<a href="mailto:balazaro1@up.edu.ph">
				<span class="icon-[solar--letter-bold] align-text-bottom text-xl"></span>
				balazaro1@up.edu.ph
			</a>
			<br />
			<a href="https://github.com/Enoux" target="_blank">
				<span class="icon-[mdi--github] align-text-bottom text-xl"></span>
				@Enoux
			</a>

			<p class="pt-2">
				Heyyy, I'm Benj! I'm a 3rd year Computer Science student from UP Diliman. I really enjoy
				software engineering and web development, but I might have learned this semester that data
				science & machine learning won't be in my top 5 skills in the near future hehe.
			</p>
			<br />
			<p>
				I tend to spend my free time playing video games or watching movies and tv series,
				especially from the mystery/thriller genre. I also enjoy going on food trips and cafe
				hopping with my friends! Cheers ☕️
			</p>
		</div>

		<div class="w-full gap-3">
			<img
				src={fibi}
				alt="Fibi Moraca"
				class="mb-2 aspect-4/5 rounded-xl border border-foodpandapink/30 object-cover"
			/>
			<p class="text-xl font-bold">Fibi Moraca</p>

			<a href="mailto:ppmoraca@up.edu.ph">
				<span class="icon-[solar--letter-bold] align-text-bottom text-xl"></span>
				ppmoraca@up.edu.ph
			</a>
			<br />
			<a href="https://github.com/dinemunyu" target="_blank">
				<span class="icon-[mdi--github] align-text-bottom text-xl"></span>
				@dinemunyu
			</a>

			<p class="pt-2">
				Hallo! Ich bin Fibi und studiere Informatik under Universität von dem Philipppinen. Mahilig
				ako gumuhit at magpinta bilang libangan sa libre kong oras.
			</p>
		</div>

		<div class="w-full gap-3">
			<img
				src={karlo}
				alt="Karlo Domingo"
				class="mb-2 aspect-4/5 rounded-xl border border-foodpandapink/30 object-cover"
			/>
			<p class="text-xl font-bold">Karlo Domingo</p>

			<a href="mailto:ksdomingo4@up.edu.ph">
				<span class="icon-[solar--letter-bold] align-text-bottom text-xl"></span>
				ksdomingo4@up.edu.ph
			</a>
			<br />
			<a href="https://github.com/krldomingo" target="_blank">
				<span class="icon-[mdi--github] align-text-bottom text-xl"></span>
				@krldomingo
			</a>

			<p class="pt-2">
				Hi! I'm Karlo, a 4th year Computer Science student from UP Diliman. I am primarily
				interested in web development, so data science has been a new and interesting, if not
				somewhat daunting, subject for me this semester.
			</p>
			<br />
			<p>
				Outside of academics, I enjoy trying all sorts of creative pursuits. I am particularly fond
				of drawing, music, and fiber arts among others. Otherwise, you might find me enjoying a good
				horror movie or cartoon series.
			</p>
		</div>
	</div>
</div>
