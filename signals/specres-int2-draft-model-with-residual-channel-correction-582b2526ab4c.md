# SpecRes: INT2 draft model with residual-channel correction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `specres-int2-draft-model-with-residual-channel-correction-582b2526ab4c`
Run ID: `specres-int2-draft-model-with-residual-channel-correction-582b2526ab4c-20260610T114058297804+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ff79ed4c30e8

## What looked useful

Calibrated residual-channel correction produced monotonic held-out KL reductions of about 10.1%, 21.2%, and 41.4% at 3.125%, 6.25%, and 12.5% residual-channel budgets, with corresponding acceptance proxy gains of about 0.0019, 0.0043, and 0.0087. Random residual channels also helped but were weaker, indicating the calibrated channel selection is a meaningful part of the mechanism.

## Boundaries and scale limits

No pretrained language model, real corpus, tokenizer, trained draft model, fused INT2 kernel, or end-to-end speculative decoding throughput was tested. Payload estimates are storage-only and do not measure runtime bandwidth, cache behavior, or kernel overhead.

## Claim scope

In a deterministic NumPy toy autoregressive proxy, adding calibration-selected high-precision residual weights for 3.125% to 12.5% of input channels improved an INT2 draft approximation to a full-precision target on held-out contexts, especially KL(target||draft) and speculative acceptance mass.

## Why it stopped

Closed as no-paper useful signal: the current evidence is a controlled toy proxy that supports the mechanism but is not direct/full validation on a pretrained LM or real speculative decoding system.

## Recommended next action

Run a bounded GPT-2-small-class real-text follow-up comparing plain INT2, INT2 plus calibrated residual channels, INT2 plus random residual channels, and INT4 using true speculative acceptance and wall-clock decode throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small real-text validation of INT2 residual-channel draft correction
- Success threshold: At equal or lower storage than an INT4 draft, calibrated INT2 plus residual channels improves true speculative acceptance by at least 5% relative over plain INT2 and retains at least 95% of INT4 decode throughput on the same hardware.
- Stop condition: Stop if calibrated residual channels fail to beat random residual channels by at least 2% relative acceptance or if runtime overhead erases the acceptance gain versus INT4.

## Evidence references

- Artifact root: `<local-path>/projects/specres-int2-draft-model-with-residual-channel-correction-582b2526ab4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
