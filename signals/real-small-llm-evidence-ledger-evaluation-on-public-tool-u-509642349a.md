# Real small-LLM evidence-ledger evaluation on public tool-use QA

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-small-llm-evidence-ledger-evaluation-on-public-tool-u-509642349a`
Run ID: `real-small-llm-evidence-ledger-evaluation-on-public-tool-u-509642349a-20260527T181443488767+0000`

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

- Parent run decision: Evidence-ledger constraint for small tool agents: enoch://control-plane/projects/evidence-ledger-constraint-for-small-tool-agents-8e6716121567/runs/evidence-ledger-constraint-for-small-tool-agents-8e6716121567-20260527T150603435550+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0f7b5307e325

## What looked useful

Ledger prompting produced fully parseable outputs but only 1/40 correct answers versus 0/40 for baseline, a +0.025 absolute delta below the +0.10 Tier 1 success threshold. The main failure mode was incorrect reasoning/arithmetic inside parseable ledgers, suggesting ledger structure alone is insufficient for this small model.

## Boundaries and scale limits

Single 0.5B instruction model; first 40 of 100 ToolQA GSM8K easy items; no external calculator execution loop; no SQL/retrieval/graph ToolQA domains; one deterministic decoding configuration.

## Claim scope

On the first 40 public ToolQA easy GSM8K calculator-style questions, Qwen/Qwen2.5-0.5B-Instruct with a structured evidence-ledger prompt did not achieve the pre-registered +0.10 absolute exact-numeric accuracy improvement over a direct-answer baseline.

## Why it stopped

Tier 1 direct test failed the stated threshold: ledger accuracy was 1/40 (0.025) versus baseline 0/40 (0.0), below the required +0.10 absolute improvement; this is early direct falsification for the tested model/split, not a full validation across ToolQA domains or larger models.

## Recommended next action

Stop the paper path for ledger-only prompting; the only concrete next bounded test is a calculator-executed ledger loop on the full 100-item ToolQA/GSM8K easy split with the same paired baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calculator-executed evidence ledgers on ToolQA/GSM8K
- Success threshold: Calculator-executed ledger improves exact numeric accuracy by at least +0.10 absolute over both direct-answer and ledger-only controls on the 100-item split, with >=0.90 parse rate.
- Stop condition: Stop if expression extraction/ledger parse rate is below 0.70 on a 10-item smoke test or if the 100-item paired run shows less than +0.05 absolute improvement over ledger-only prompting.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-llm-evidence-ledger-evaluation-on-public-tool-u-509642349a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
