# N-gram Contextual Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-contextual-drafting-32ea40b511f2`
Run ID: `n-gram-contextual-drafting-32ea40b511f2-20260523T203202864313+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/71f733db03f9

## What looked useful

The mechanism gives large ideal target-call reductions on copy-heavy contexts, around 62% in the main setting, but only about 3% on natural prose with min_ngram=3 and max_draft=16. Sweep results show natural-prose gains remain small while copy-heavy gains are persistent.

## Boundaries and scale limits

No real transformer runtime, tokenizer-specific serving stack, batching, or wall-clock latency was tested. Natural text coverage was limited to two public-domain books; copy-heavy workloads were controlled variants.

## Claim scope

Prompt-local n-gram contextual drafting was tested as exact-token continuation lookup over two Project Gutenberg texts and controlled copy/near-copy variants, using a non-overlapping oracle decode-loop proxy.

## Why it stopped

Proxy evidence supports a narrow copy-heavy mechanism but does not support a broad or publication-grade claim for general n-gram contextual drafting.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should measure end-to-end latency in a small transformer generation loop on copy-heavy and natural workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end latency test for prompt-local n-gram drafting
- Success threshold: At least 25% measured latency improvement on copy-heavy prompts with unchanged generated text, and explicit measurement showing whether natural prose remains below 10% improvement.
- Stop condition: Stop if lookup plus verification overhead erases the copy-heavy gain or if natural-prose acceptance remains too sparse to produce measurable speedup.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-contextual-drafting-32ea40b511f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
