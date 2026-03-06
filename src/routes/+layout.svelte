<script lang="ts">
	import './layout.css';

	const { children } = $props();

	export const prerender = true;
</script>

{@render children()}
