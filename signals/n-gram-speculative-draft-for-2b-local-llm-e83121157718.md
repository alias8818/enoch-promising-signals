# N-gram Speculative Draft for 2B Local LLM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-2b-local-llm-e83121157718`
Run ID: `n-gram-speculative-draft-for-2b-local-llm-e83121157718-20260524T195842126110+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c0d6a6b220fe

## What looked useful

Simulated exact validation reached 1.67 effective tokens per target validation call overall, with about 2.03 on code-like prompts, 2.02 on repetitive prompts, and 1.24 on general prose. A Transformers prompt_lookup wall-clock run was 1.59x-1.74x faster in tokens/s but did not consistently match greedy outputs, so it is speed-potential evidence only.

## Boundaries and scale limits

One 2B-class model, 8 prompts, 378 simulated target tokens for acceptance analysis, and a short 2-repeat wall-clock benchmark. No large prompt corpus, no batched serving test, no quantized-model comparison, and no verified production exact speculative decoding kernel.

## Claim scope

On 8 short handcrafted prompts with HuggingFaceTB/SmolLM2-1.7B-Instruct on GB10, a prompt-history n-gram drafter produced useful exact-token acceptance potential for repetitive and code-like contexts but weak gains for general prose. The result supports a bounded mechanism signal, not a broad local-LLM serving claim.

## Why it stopped

Bounded local evidence is mixed: the n-gram mechanism works for copy-heavy/code contexts, but general prose is weak and the wall-clock library path was not consistently output-identical to greedy generation.

## Recommended next action

Stop this run as no-paper useful signal; next run should verify an exact greedy-preserving prompt-lookup speculative decoder on a larger real prompt corpus before claiming practical speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact prompt-lookup speculative decoding on a real 2B local prompt suite
- Success threshold: Token-identical outputs with at least 1.3x median wall-clock speedup on code/repetitive domains and no more than 5% median slowdown on general prose.
- Stop condition: Stop if output identity cannot be guaranteed or if median wall-clock speedup is below 1.1x on code/repetitive prompts after implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-2b-local-llm-e83121157718`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
