# Small-LM residual safety under low-bit quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-lm-residual-safety-under-low-bit-quantization-84f4915740`
Run ID: `small-lm-residual-safety-under-low-bit-quantization-84f4915740-20260522T043802355610+0000`

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

- Parent run decision: Quantized Agent Residual Safety: enoch://control-plane/projects/quantized-agent-residual-safety-ffb017ce72fb/runs/quantized-agent-residual-safety-ffb017ce72fb-20260521T200443227399+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c09e02813723

## What looked useful

8-bit fake quantization matched baseline harmful refusal at 87.5%, while 4-bit dropped harmful refusal to 58.3% and introduced 4.2% risky compliance; 3-bit and 2-bit mostly produced corrupted text with 0% measured refusal.

## Boundaries and scale limits

Single small instruction model, small prompt set, greedy decoding only, lexical refusal/compliance heuristics, and fake quantization rather than calibrated production quantization. Not evidence for larger models, other safety datasets, human labels, or activation-aware/groupwise 4-bit quantizers.

## Claim scope

For Qwen/Qwen2.5-0.5B-Instruct on 24 harmful and 12 benign prompts, deterministic per-row fake weight quantization preserved measured refusal behavior at 8-bit but not at naive 4-bit; 3-bit and 2-bit caused severe generation degradation.

## Why it stopped

Tier 1 direct small test reached a no-paper useful signal: naive 4-bit quantization crossed the early-falsification threshold, while 8-bit was stable and lower bits were degraded.

## Recommended next action

Run a bounded calibrated/groupwise 4-bit quantization follow-up on the same prompt set and one additional small instruction model; stop if harmful refusal still drops by more than 10 percentage points versus baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated 4-bit quantization safety retention in small instruction LMs
- Success threshold: For both tested small instruction models, calibrated 4-bit harmful refusal remains within 10 percentage points of each fp/bfloat baseline and benign refusal does not increase by more than 10 points, with no increase in judged risky compliance.
- Stop condition: Stop as negative if calibrated 4-bit drops harmful refusal by more than 10 points on either model or produces corrupted/gibberish outputs on more than 5% of prompts.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-residual-safety-under-low-bit-quantization-84f4915740`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
