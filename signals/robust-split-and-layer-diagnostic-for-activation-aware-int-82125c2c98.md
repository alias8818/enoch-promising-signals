# Robust split-and-layer diagnostic for activation-aware INT2 residual salience on GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `robust-split-and-layer-diagnostic-for-activation-aware-int-82125c2c98`
Run ID: `robust-split-and-layer-diagnostic-for-activation-aware-int-82125c2c98-20260523T125449718377+0000`

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

- Parent run decision: INT2 Agent Weights with Residual Salience Channels: enoch://control-plane/projects/int2-agent-weights-with-residual-salience-channels-d340cf469718/runs/int2-agent-weights-with-residual-salience-channels-d340cf469718-20260523T112545230441+0000
- Parent run decision: Activation-aware INT2 residual salience on GPT-2 linear weights: enoch://control-plane/projects/activation-aware-int2-residual-salience-on-gpt-2-linear-we-85cf4f46d1/runs/activation-aware-int2-residual-salience-on-gpt-2-linear-we-85cf4f46d1-20260523T124002690437+0000

## What looked useful

The diagnostic found real layer/split salience: matched activation-aware INT2 improved 10/12 isolated attention layer ablations and 12/12 isolated MLP layer ablations, and attention-only quantization improved from +3.9805 to +2.4998 mean delta NLL. The full-model result was negative for the tested method: matched activation-aware INT2 worsened mean delta NLL from +5.4217 to +6.1533, while shuffled-RMS control improved to +4.8030, so the mechanism is non-compositional or mis-specified at full-model scope.

## Boundaries and scale limits

Single model scale (GPT-2-small), single dataset (WikiText-2 raw test), 96 calibration windows, 64 evaluation windows for each of 3 fixed seeds, one signed INT2 grid, one group size, and one activation exponent. No 7B+ model, no downstream tasks, no full calibration sweep, and no production quantization kernel validation.

## Claim scope

On GPT-2-small evaluated on fixed WikiText-2 raw test windows, matched activation-RMS INT2 reweighting reduces loss damage for many isolated layer/split ablations, especially attention-only and per-layer MLP cases, but does not improve full-model INT2 quantization versus a weight-only baseline.

## Why it stopped

Tier 2 direct GPT-2-small evidence is mixed and fails the full-model activation-aware INT2 improvement criterion, despite useful isolated layer/split mechanism signal.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should sweep activation exponent/group policy and composition-aware mixed quantization while retaining weight-only and shuffled-RMS controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Composition-aware activation exponent sweep for GPT-2 INT2 layer/split quantization
- Success threshold: A selected activation-aware or mixed policy reduces full-model mean delta NLL by at least 0.25 versus weight-only INT2 and at least 0.10 versus shuffled-RMS control across all three fixed seeds, while preserving the isolated layer/split salience pattern.
- Stop condition: Stop if no alpha or split-specific policy beats both weight-only and shuffled-RMS full-model controls on all fixed seeds, even if isolated layer ablations remain positive.

## Evidence references

- Artifact root: `<local-path>/projects/robust-split-and-layer-diagnostic-for-activation-aware-int-82125c2c98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
