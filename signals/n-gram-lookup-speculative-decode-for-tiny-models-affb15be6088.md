# N-Gram Lookup Speculative Decode for Tiny Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-lookup-speculative-decode-for-tiny-models-affb15be6088`
Run ID: `n-gram-lookup-speculative-decode-for-tiny-models-affb15be6088-20260605T041643967842+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9386228f9296

## What looked useful

Lookup drafts are a real mechanism for copy-heavy tiny-model decoding, reaching 84.4% mean target-pass reduction and 1.15x wall-clock speedup on repeat-heavy prompts at gamma=8, but ordinary prompts averaged only 14.6% pass reduction and 0.53x wall-clock speed at gamma=8.

## Boundaries and scale limits

Nine hand-authored prompts, 32 generated tokens each, distilgpt2 plus smoke tests on sshleifer/tiny-gpt2; prototype uses full-prefix verification rather than an optimized KV-cached speculative verifier; no large corpus, stochastic decoding, or production serving stack was tested.

## Claim scope

On a GB10 local benchmark with distilgpt2 greedy decoding, dynamic n-gram lookup speculative decoding exactly matches greedy output and substantially reduces target passes only for repeat-heavy prompts; ordinary prompts show small pass reductions and slower wall-clock performance in the prototype.

## Why it stopped

Mixed bounded evidence: the mechanism works on repeat-heavy prompts, but ordinary tiny-model prompts do not show useful wall-clock speed in this prototype.

## Recommended next action

Stop this run as no-paper useful signal; the bounded next test is a KV-cached verifier on a realistic repeated-context corpus, not a paper write-up from the current evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-Cached N-Gram Lookup Speculative Decode on Realistic Repeated Contexts
- Success threshold: Exact greedy equality on all evaluated prompts, median wall-clock speedup >= 1.2x, target-pass reduction >= 40%, and no p95 regression below 0.9x on ordinary prompts.
- Stop condition: Stop if KV-cached verification still gives median speedup below 1.0x or if non-handpicked prompts keep target-pass reduction below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-lookup-speculative-decode-for-tiny-models-affb15be6088`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
