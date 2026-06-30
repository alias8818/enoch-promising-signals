# KV-cache confidence-gated suffix drafting on larger target models

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `kv-cache-confidence-gated-suffix-drafting-on-larger-target-a247dd0292`
Run ID: `kv-cache-confidence-gated-suffix-drafting-on-larger-target-a247dd0292-20260524T054626086527+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-corpus suffix-index drafting with strong retrieval baselines: enoch://control-plane/projects/real-corpus-suffix-index-drafting-with-strong-retrieval-ba-7f40914aa9/runs/real-corpus-suffix-index-drafting-with-strong-retrieval-ba-7f40914aa9-20260524T050803717795+0000
- Parent run decision: Confidence-gated suffix drafting as an opportunistic hybrid drafter: enoch://control-plane/projects/confidence-gated-suffix-drafting-as-an-opportunistic-hybri-2be5f9e711/runs/confidence-gated-suffix-drafting-as-an-opportunistic-hybri-2be5f9e711-20260524T053343427987+0000

## What looked useful

The mechanism is real but not paper-ready: confidence gating selects suffix opportunities with nonzero acceptance, yet the implementation trades extra target verification work and assistant passes for only a small speed signal near timing-noise controls, and reduced precision breaks exactness.

## Boundaries and scale limits

Validated directly only on GPT-2-medium for 512 emitted tokens across 8 prompts. GPT-2-large confirmation did not complete because model download/loading stalled before GPU inference. No 7B+, production serving, multi-request batching, optimized kernel, or broad prompt-distribution validation was performed. Float16 gated variants failed exact greedy equivalence.

## Claim scope

On GPT-2-medium with distilGPT-2 as assistant, fixed prompts, fixed seed, and float32 cached greedy decoding, confidence-gated suffix drafting can accept verified suffix tokens while exactly matching greedy output, but the best observed wall-clock gain was only 1.060x and target token work increased by about 41%.

## Why it stopped

No-paper useful signal: direct GPT-2-medium evidence supports the acceptance mechanism but not a robust speedup or paper-readiness claim, and float16 exactness failure weakens deployment viability.

## Recommended next action

Stop this depth-4 follow-up chain; only revisit as a separately provisioned optimized serving benchmark if exact reduced-precision verification and a larger-target baseline can be tested.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-confidence-gated-suffix-drafting-on-larger-target-a247dd0292`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
