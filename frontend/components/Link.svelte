<script context="module">
	export const evidenceInclude = true;
</script>

<script>
	import { getContext, onDestroy, onMount } from 'svelte';

    /**
	 * @type {string}
	 */
	export let dest;

    /**
	 * @type {string}
	 */
	export let text;

	/**
	 * @type {import("svelte/store").Writable<{ links: {dest: string, text: string}[]}>}
	 */
	const links = getContext('LINK_REGISTRATION');

    onMount(() => {
		$links.links = [...$links.links, { dest, text }];
    });

</script>

<!--- TODO: Is there a better way to use the interior of a <Link> text </Link> object here instead of 'text'? ---> 