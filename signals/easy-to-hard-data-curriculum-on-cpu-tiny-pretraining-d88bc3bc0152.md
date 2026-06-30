# Easy-to-hard data curriculum on CPU tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `easy-to-hard-data-curriculum-on-cpu-tiny-pretraining-d88bc3bc0152`
Run ID: `easy-to-hard-data-curriculum-on-cpu-tiny-pretraining-d88bc3bc0152-20260610T094559211938+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/75d3b4893976

## What looked useful

Mixed sampling achieved mean held-out loss 3.0888 +/- 0.0023. Easy-to-hard achieved 3.6234 +/- 0.0018, worse by +0.5346 nats in all 5 paired seeds. Hard-to-easy was worse by +0.8760 nats. The easy-to-hard schedule improved the hard slice but degraded easy/medium enough to lose the target mixed validation distribution.

## Boundaries and scale limits

Synthetic Markov data, previous-token softmax model, 48-token vocabulary, 1200 optimizer steps, 5 seeds, CPU-only. Does not validate natural-language corpora, transformer architectures, larger models, or replay/interleaved curricula.

## Claim scope

In a NumPy CPU tiny previous-token language-model proxy with synthetic Markov difficulty bands, a naive fixed-phase easy-to-hard curriculum under a matched token budget loses to uniform mixed difficulty sampling on mean held-out negative log-likelihood.

## Why it stopped

Proxy early falsification: the simple easy-to-hard curriculum was consistently worse than mixed sampling under matched optimizer steps and token budget, so this run is useful no-paper evidence rather than full validation.

## Recommended next action

Stop this naive phased-curriculum claim; if continuing, run a bounded replay/interleaving curriculum test on the same proxy before spending compute on real-text transformer pretraining.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-interleaved easy-to-hard curriculum for tiny LM pretraining
- Success threshold: Replay curriculum mean held-out loss is at least 0.02 nats lower than mixed, or statistically tied within 0.01 nats while no difficulty slice is worse by more than 0.03 nats.
- Stop condition: Stop if replay curriculum remains worse than mixed by more than 0.02 nats mean loss in at least 4 of 5 paired seeds or if it still sacrifices any non-final difficulty slice by more than 0.10 nats.

## Evidence references

- Artifact root: `<local-path>/projects/easy-to-hard-data-curriculum-on-cpu-tiny-pretraining-d88bc3bc0152`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
