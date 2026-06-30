# Coreset Data Selection for 10M Parameter GPT-2-class Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `coreset-data-selection-for-10m-parameter-gpt-2-class-pretraining-27e94e18e508`
Run ID: `coreset-data-selection-for-10m-parameter-gpt-2-class-pretraining-27e94e18e508-20260608T001901779667+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e3a7643c1d8a

## What looked useful

Equal-document coreset comparisons can be badly confounded by document length. Token-budget matching changed hashed k-center from a large apparent negative to a small consistent positive, but the mean gain was only 0.006 nats versus the predeclared 0.03 nats useful-signal threshold.

## Boundaries and scale limits

Single small corpus, 128-token context, 4096-token local BPE vocabulary, 240 steps per method, 3 seeds, simple hashed character n-gram features only; not a full 10M-parameter pretraining validation and not evidence for larger models or longer training.

## Claim scope

On WikiText-2 with an 8.7M-parameter GPT-2-class causal LM trained for 240 optimizer steps, hashed character n-gram k-center selection is harmful under equal document count because it collapses the unique-token budget; under matched 160k unique-token budget it gives a consistent but tiny validation-loss improvement over random selection across three seeds.

## Why it stopped

Bounded direct probe found only a tiny fair-budget gain and a strong document-length confound, so the evidence is useful but insufficient for a paper-positive claim.

## Recommended next action

Stop this run as no-paper evidence; a bounded follow-up should test token-budget-matched, length-regularized or semantic coreset selectors for at least 1000 steps and require at least 0.03 nats validation-loss gain over random.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-budget-matched semantic and length-regularized coreset selection for small GPT pretraining
- Success threshold: Mean validation loss at least 0.03 nats lower than random with no seed worse than random by more than 0.01 nats.
- Stop condition: Stop if token-budget-matched selectors fail to exceed random by 0.01 nats after 1000 steps or if gains are explained solely by document-length distribution.

## Evidence references

- Artifact root: `<local-path>/projects/coreset-data-selection-for-10m-parameter-gpt-2-class-pretraining-27e94e18e508`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
