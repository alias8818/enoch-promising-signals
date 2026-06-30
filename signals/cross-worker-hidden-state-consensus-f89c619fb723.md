# Cross-Worker Hidden State Consensus

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cross-worker-hidden-state-consensus-f89c619fb723`
Run ID: `cross-worker-hidden-state-consensus-f89c619fb723-20260601T062751759535+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7c1ce4c99f51

## What looked useful

Correct cross-worker hidden-state consensus reduced held-out MSE by 7.71% versus no consensus across 5/5 seeds and by 68.28% versus shuffled wrong-sequence consensus, suggesting the mechanism can help when workers hold complementary noisy views of a shared latent state.

## Boundaries and scale limits

Toy synthetic data only; 5 seeds; hidden_dim 32; seq_len 24; 280 training steps per condition; CPU-only local run. Does not validate transformer hidden states, LLM workers, multi-node training, production inference, learned communication, or real datasets.

## Claim scope

On a small synthetic AR(1) shared-latent sequence benchmark with 4 workers, noisy worker-specific observations, and a shared GRU worker model, within-sequence hidden-state averaging improved held-out latent-state MSE versus no hidden-state exchange and beat a shuffled-consensus control.

## Why it stopped

Synthetic evidence supports the mechanism but is not direct enough for a paper-positive claim about real model workers or large hidden states.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on a small real sequence modeling task with partitioned observations and the same no-consensus, correct-consensus, and shuffled-consensus controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Partitioned Real-Sequence Hidden-State Consensus Benchmark
- Success threshold: Correct consensus must improve validation loss or perplexity by at least 3% versus no consensus on the mean across seeds, win on at least 3 of 3 seeds, and beat shuffled consensus by at least 10%.
- Stop condition: Stop if correct consensus fails to beat no consensus on at least 2 of 3 seeds or if shuffled consensus matches correct consensus within 2%, because that would suggest the synthetic gain does not transfer beyond the toy latent process.

## Evidence references

- Artifact root: `<local-path>/projects/cross-worker-hidden-state-consensus-f89c619fb723`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
