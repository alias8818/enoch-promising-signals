# Hidden-State Linear Extrapolation for Zero-Parameter Draft Tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hidden-state-linear-extrapolation-for-zero-parameter-draft-tokens-79a1ed9caa91`
Run ID: `hidden-state-linear-extrapolation-for-zero-parameter-draft-tokens-79a1ed9caa91-20260528T154551342341+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/233ff68cbe05

## What looked useful

The mechanism has a small measurable above-control signal on a real frozen LM, but the fixed constant-velocity rule is far too weak as a practical draft-token method in this test and the best alpha contradicts the original alpha=1 intuition.

## Boundaries and scale limits

Small pretrained GPT-family model, local deterministic corpus, greedy decoding only, acceptance-only measurement without optimized speculative decoding latency, no 7B+ or broad benchmark validation.

## Claim scope

On a bounded distilgpt2 greedy second-token probe with 4096 local prose prefixes, fixed zero-parameter hidden-state linear extrapolation at alpha=1 produced only 3.37% draft acceptance versus 2.54% persistence/repeat controls; an oracle alpha grid peaked at 5.35% with alpha=-0.5.

## Why it stopped

Early proxy falsification rather than full validation: the direct distilgpt2 acceptance test showed fixed alpha=1 acceptance of only 3.37%, too low for a useful speculative decoding claim.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a follow-up if it tests alpha-swept or rule-selected zero-parameter hidden extrapolation on a broader prompt suite with a predefined acceptance threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Alpha-selected zero-parameter hidden extrapolation on broader pretrained LM prompts
- Success threshold: Calibrated zero-parameter extrapolation reaches at least 10% test acceptance and at least 2x persistence acceptance on every tested model/domain pair.
- Stop condition: Stop if calibrated alpha fails to reach 10% acceptance or fails to beat persistence by 2x on any tested model/domain pair.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-linear-extrapolation-for-zero-parameter-draft-tokens-79a1ed9caa91`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
