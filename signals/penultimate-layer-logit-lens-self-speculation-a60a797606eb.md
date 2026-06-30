# Penultimate-Layer Logit-Lens Self-Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `penultimate-layer-logit-lens-self-speculation-a60a797606eb`
Run ID: `penultimate-layer-logit-lens-self-speculation-a60a797606eb-20260528T171013243280+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1649e0e8edf2

## What looked useful

The penultimate hidden state is closer to final logits than earlier layers, but untuned logit-lens agreement is too low for useful self-speculative speedup in this bounded probe.

## Boundaries and scale limits

Single small pretrained model, 10 fixed prompts, 292 next-token positions, 30 speculative contexts, CPU inference, analytical cost model rather than a true truncated-forward serving implementation.

## Claim scope

On distilgpt2 with an untuned penultimate-layer logit lens, greedy self-speculative drafting is not practically viable: 45.5% top-1 agreement and 0.97 accepted tokens per 4-token draft fall far below the optimistic break-even threshold of 3.33 accepted tokens.

## Why it stopped

Early direct small-model falsification of the practical speed claim; this is not a full validation across model scales or tuned self-speculation methods.

## Recommended next action

Stop this no-paper run; only pursue a follow-up if testing a trained/tuned lens or true truncated-draft implementation with an explicit break-even threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tuned Internal Lens for Self-Speculative Drafting
- Success threshold: Measured end-to-end greedy decoding speedup greater than 1.10x with no change in final greedy output on at least 1,000 held-out contexts, or accepted prefix length exceeding the measured break-even threshold by at least 10%.
- Stop condition: Stop if tuned-lens accepted prefix length remains below break-even or measured end-to-end speed is not faster than greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/penultimate-layer-logit-lens-self-speculation-a60a797606eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
