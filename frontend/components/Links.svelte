<script context="module">
	export const evidenceInclude = true;
</script>

<script>
	import { onMount, setContext } from 'svelte';
	import { writable } from 'svelte/store';

	/**
	 * @type {import("svelte/store").Writable<{ links: {dest: string, text: string}[]}>}
	 */
	const linkItems = writable({ links: [] });

	onMount(() => {
	
	});

	setContext('LINK_REGISTRATION', linkItems);

</script>

<div class="text-center card">
	<p>
	{#each $linkItems.links as link, i}
		{#if i > 0}&nbsp;|{/if}
		<a href="{link.dest}">
			{link.text}
		</a>
	{/each}
	</p>
	<div>
		<!--- TODO: Why is this needed? ---> 
		<slot />
	</div>
</div>

