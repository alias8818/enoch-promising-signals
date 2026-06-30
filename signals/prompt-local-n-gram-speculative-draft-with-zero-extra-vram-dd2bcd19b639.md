# Prompt-Local N-gram Speculative Draft with Zero Extra VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-local-n-gram-speculative-draft-with-zero-extra-vram-dd2bcd19b639`
Run ID: `prompt-local-n-gram-speculative-draft-with-zero-extra-vram-dd2bcd19b639-20260523T172804422412+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7d1a8c055254

## What looked useful

Prompt-only n-gram drafting achieved exact greedy equivalence with 0.372 mean acceptance and 0.370 mean target-forward reduction on distilgpt2; copy/template prompts were strong (0.686 acceptance, 0.729 forward reduction) while open prompts were weak (0.057 acceptance, 0.010 forward reduction). Prompt+generated indexing reached 0.780 acceptance and 0.676 forward reduction but appears driven partly by repetitive model continuations.

## Boundaries and scale limits

Only 8 handcrafted prompts, distilgpt2 plus tiny-gpt2 smoke, greedy decoding, no production KV-cache integration, no batching, no real serving traffic, no 7B+ validation.

## Claim scope

Small local distilgpt2 greedy-decoding probe: a CPU prompt-local n-gram drafter preserves exact greedy output and reduces target forwards on repetitive/template prompts, but prompt-only drafting provides little benefit on open-ended prompts.

## Why it stopped

No-paper useful signal: the bounded probe supports the mechanism on repetitive prompts but is too small and too synthetic for a publication-grade or broad serving claim.

## Recommended next action

Run a bounded KV-cache-aware verifier on a small real prompt corpus and compare p50/p95 latency, acceptance, and memory deltas against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache prompt-local n-gram speculative decoding on real prompts
- Success threshold: Exact output match on all prompts, at least 10% p50 latency reduction on repetitive/template prompts, no more than 2% peak CUDA memory increase, and no more than 5% p95 latency regression on open-ended prompts.
- Stop condition: Stop if exact greedy equivalence fails, if CPU n-gram overhead removes latency gains on repetitive prompts, or if open-ended prompts show consistent p95 latency regressions above 5%.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-local-n-gram-speculative-draft-with-zero-extra-vram-dd2bcd19b639`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
