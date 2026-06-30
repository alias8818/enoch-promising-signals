# N-Gram Speculative Draft for Local Model Cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-local-model-cascades-03f3ff7f6cd2`
Run ID: `n-gram-speculative-draft-for-local-model-cascades-03f3ff7f6cd2-20260601T075851194027+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5734810fcadd

## What looked useful

Same-domain 3-4 gram drafts reached 4.32-6.49 ideal tokens per target call with 76.8%-84.6% ideal target-call reduction in the proxy, while a domain-shift control collapsed to about 1.6% reduction and 98.4% zero-accept calls.

## Boundaries and scale limits

Two small public text corpora, word-level tokenization, deterministic greedy n-gram verifier, no GPU inference, no KV-cache or wall-clock neural decoding measurement, and no comparison to a trained neural draft model.

## Claim scope

Bounded CPU proxy: lower-order n-gram draft models can reduce ideal target calls against a same-domain 5-gram verifier, but this was not tested on a neural local model or real serving stack.

## Why it stopped

No-paper closure: current evidence is a useful proxy mechanism result, not direct/full validation of n-gram speculative drafting for local neural model cascades.

## Recommended next action

Run a bounded direct neural validation using a GPT-2-small-class or local small model tokenizer, comparing n-gram draft cache wall-clock tokens/sec against greedy decoding and a small neural draft baseline on in-domain and domain-shift prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct neural validation of same-context n-gram speculative draft caches
- Success threshold: At least 20% wall-clock tokens/sec improvement over greedy decoding on same-domain prompts with no more than 5% degradation on domain-shift prompts, after including draft overhead.
- Stop condition: Stop if accepted tokens per target pass is below 1.2 or wall-clock throughput fails to exceed greedy decoding by 10% on same-domain prompts after overhead.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-local-model-cascades-03f3ff7f6cd2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
