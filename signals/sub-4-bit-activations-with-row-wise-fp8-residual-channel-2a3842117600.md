# Sub-4-bit activations with row-wise FP8 residual channel

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `sub-4-bit-activations-with-row-wise-fp8-residual-channel-2a3842117600`
Run ID: `sub-4-bit-activations-with-row-wise-fp8-residual-channel-2a3842117600-20260630T065052793470+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0d3cbbec0553

## What looked useful

Sparse FP8 residuals are a weak correction for INT3 activations: best tested output-aware k=32 reduced mean projection NMSE from 0.346994 to 0.298615, but INT4 was 0.208428 under the same captured activations.

## Boundaries and scale limits

No full quantized inference kernel, perplexity run, downstream evaluation, fine-tuning, or 7B-scale model was tested. Metrics are one-step activation reconstruction and projection-output NMSE on a GPT-2-class model.

## Claim scope

On 24 distilgpt2 attention/MLP projection activation inputs, row-wise INT3 plus sparse top-k FP8 residual corrections improves INT3 projection error but remains materially worse than row-wise INT4 for k up to 32, about 3.615 estimated activation bits.

## Why it stopped

Bounded real-activation proxy falsified the practical quality claim: the mechanism helps INT3 but does not close the gap to a simpler INT4 baseline.

## Recommended next action

Stop this format as a paper path unless a separate calibrated inference-quality experiment shows INT3 plus sparse FP8 residual bookkeeping beats plain INT4 on perplexity and runtime.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/sub-4-bit-activations-with-row-wise-fp8-residual-channel-2a3842117600`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
